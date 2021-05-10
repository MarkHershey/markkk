import os
import shlex
import shutil
import subprocess
from multiprocessing import Pool
from pathlib import Path
from typing import List, Tuple

from .logger import loggers


def safe_rename(src: str, dest: str):
    """
    safety checks:
        1. check if source exists before rename
        2. check if new name destination already exist before rename
    Only rename file when passing above two checks
    """
    src = Path(src)
    dest = Path(dest)

    if not Path(src).exists():
        logger.error(
            f"safe_rename cannot be done, because source file '{src}' not found."
        )
        return
    if Path(dest).exists():
        logger.error(
            f"safe_rename cannot be done, because destination file '{dest}' already exist."
        )
        return
    try:
        os.rename(src, dest)
        logger.debug(f"'{src}' has been renamed to '{dest}'")
    except Exception as err:
        logger.error(f"Rename operation failed, reason: {err}")


def safe_copy(src: str, dest: str):
    """
    safety checks:
        1. check if source exists before copy
        2. check if same-name file already exist in destination before copy
    Only copy file when passing above two checks
    """
    src = Path(src)
    dest = Path(dest)

    if not Path(src).exists():
        logger.error(
            f"safe_copy cannot be done, because source file '{src}' not found."
        )
        return
    if Path(dest).exists():
        logger.warning(
            f"safe_copy cannot be done, because destination file '{dest}' already exist."
        )
        return
    try:
        # subprocess.run(["cp", str(src), str(dest)])
        shutil.copy2(src, dest)
        logger.debug(f"'{src}' has been copied to '{dest}'")
    except Exception as err:
        logger.error(f"Copy operation failed, reason: {err}")


def safe_move(src: str, dest: str):
    """
    safety checks:
        1. check if source exists before move
        2. check if same-name file already exist in destination before move
    Only move file when passing above two checks
    """
    src = Path(src)
    dest = Path(dest)

    if not Path(src).exists():
        logger.error(
            f"safe_move cannot be done, because source file '{src}' not found."
        )
        return
    if Path(dest).exists():
        logger.warning(
            f"safe_move cannot be done, because destination file '{dest}' already exist."
        )
        return
    try:
        os.move(src, dest)
        logger.debug(f"'{src}' has been moved to '{dest}'")
    except Exception as err:
        logger.error(f"Move operation failed, reason: {err}")


class MassCopier:
    CopyJob = Tuple[str, str]
    verbose = True
    overwrite = False
    large_files = False

    def __init__(self):
        self.copy_jobs: List[MassCopier.CopyJob] = []

    def add(self, src: str, dst: str):
        src = Path(src)
        if not src.exists():
            logger.error(f"Source file '{src}' not found.")
            return

        dst = Path(dst).resolve()
        if dst.is_file():
            logger.warning(f"Destination path has existing file '{dst}'.")
        elif dst.is_dir():
            dst = dst / src.name
            if dst.is_file():
                dst = str(dst)
                logger.warning(f"Destination path has existing file '{dst}'.")

        src = str(src)
        dst = str(dst)
        self.copy_jobs.append((src, dst))

    @staticmethod
    def make_copy(copy_job: CopyJob):
        src, dst = copy_job

        if MassCopier.large_files:
            tmp_dst = str(dst) + ".tmp"
        else:
            tmp_dst = str(dst)

        flags = "-"
        if MassCopier.verbose:
            flags += "v"
        if MassCopier.overwrite:
            flags += "f"
        else:
            flags += "n"

        completed = subprocess.run(
            args=shlex.split(f'cp {flags} "{src}" "{tmp_dst}"'),
            # stdout=subprocess.PIPE,
        )
        failed = True if completed.returncode != 0 else False

        if failed:
            logger.error(f"Failed job: ({src}) -> ({dst})")
            return copy_job
        else:
            # logger.debug(f"Succeeded job: ({src}) -> ({dst})")
            if MassCopier.large_files:
                completed = subprocess.run(
                    args=shlex.split(f'mv {flags} "{tmp_dst}" "{dst}"'),
                    # stdout=subprocess.PIPE,
                )
            return "OK"

    def start(
        self,
        interactive: bool = False,
        verbose: bool = True,
        overwrite: bool = False,
        large_files: bool = False,
    ):
        MassCopier.verbose = verbose
        MassCopier.overwrite = overwrite
        MassCopier.large_files = large_files

        if verbose:
            print(f"Number of files to be copied: {len(self.copy_jobs)}")
            if overwrite:
                print("Overwrite Mode")
            else:
                print("Safe Mode (Strictly do not overwrite)")

            if large_files:
                print("Large Files Mode (Prevent incomplete transfer)")
            else:
                print("Regular Files Mode (Do not prevent incomplete transfer)")

            if verbose:
                print("Verbose Mode")

        if interactive:
            _start = str(input("Start to copy (y/n)? ")).strip()
            if _start != "y":
                logger.warning("Operation aborted by instruction.")
                return

        pool = Pool()
        result = pool.map(MassCopier.make_copy, self.copy_jobs)
        if verbose:
            print(list(result))


if __name__ == "__main__":
    cp = MassCopier()
    cp.add("...", "...")
    cp.start(1, 1, 0, 1)
