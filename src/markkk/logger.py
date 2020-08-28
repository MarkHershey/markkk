import os
import logging
import colorlog
from pathlib import Path

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

log_dir = Path("logs/")

if not log_dir.is_dir():
    os.mkdir(log_dir)

debug_log_fp = log_dir / "debug.log"
error_log_fp = log_dir / "error.log"

fh1 = logging.FileHandler(debug_log_fp, mode="a")
fh1.setLevel(logging.DEBUG)
fh2 = logging.FileHandler(error_log_fp, mode="a")
fh2.setLevel(logging.ERROR)
sh = colorlog.StreamHandler()
sh.setLevel(logging.DEBUG)

# Define formatters
formatter = logging.Formatter(
    fmt="%(asctime)s - %(levelname)-8s | %(filename)s:%(lineno)s | %(message)s ",
    datefmt="%Y-%m-%d %H:%M:%S",
)
color_formatter = colorlog.ColoredFormatter(
    fmt="%(log_color)s%(levelname)-8s%(reset)s %(log_color)s%(message)s %(black)s(%(filename)s:%(lineno)s)",
    datefmt=None,
    reset=True,
    log_colors={
        "DEBUG": "green",
        "INFO": "cyan",
        "WARNING": "yellow",
        "ERROR": "red",
        "CRITICAL": "red,bg_yellow",
    },
    secondary_log_colors={},
    style="%",
)

# Set the formatter for each handler
fh1.setFormatter(formatter)
fh2.setFormatter(formatter)
sh.setFormatter(color_formatter)

# Add all three handlers to the logger
logger.addHandler(fh1)
logger.addHandler(fh2)
logger.addHandler(sh)

if __name__ == "__main__":
    logger.debug("This is a debug message")
    logger.info("This is a message for your information")
    logger.warning("This is a warning message")
    logger.error("This is an error message")
    logger.critical("This is a critical error message")
