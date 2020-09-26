import os
from pathlib import Path
from .logger import logger


def safe_rename(src: str, dest: str):
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
