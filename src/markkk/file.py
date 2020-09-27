import os
import shutil
from pathlib import Path

from .logger import logger


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
