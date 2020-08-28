import logging
import colorlog

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

fh1 = logging.FileHandler("log_debug.log", mode="a")
fh1.setLevel(logging.DEBUG)
fh2 = logging.FileHandler("log_error.log", mode="a")
fh2.setLevel(logging.ERROR)
sh = colorlog.StreamHandler()
sh.setLevel(logging.DEBUG)

# Define formatters
formatter = logging.Formatter("%(asctime)s - %(levelname)-8s - %(message)s")
color_formatter = colorlog.ColoredFormatter(
    "%(log_color)s%(levelname)-8s%(reset)s %(log_color)s%(message)s",
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
