import logging as lg
from pathlib import Path

from rich.logging import RichHandler

from .constant import BASE_DIR

logger = lg.getLogger(__file__)
rich_handeler = RichHandler()
formater = lg.Formatter(
    "%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(message)s"
)
rich_handeler.setFormatter(formater)
rich_handeler.setLevel(lg.DEBUG)
logger.addHandler(rich_handeler)
logger.setLevel(lg.DEBUG)


def logger_factory(name: str) -> lg.Logger:
    logger.info(f"Trying to make a logger - name:{name}")
    new_logger = lg.getLogger(name)

    logger.debug("Make handlers.")
    rich_han = RichHandler()
    file_handeler = lg.FileHandler(BASE_DIR / "logs" / f"{name}.log")

    logger.debug("Make formatters.")
    formaterr = lg.Formatter(
        "%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(message)s"
    )

    logger.debug("Set level on handlers.")
    rich_han.setLevel(lg.DEBUG)
    file_handeler.setLevel(lg.DEBUG)
    new_logger.setLevel(lg.DEBUG)

    logger.debug("Set formatter on handlers.")
    rich_han.setFormatter(formaterr)
    file_handeler.setFormatter(formaterr)

    logger.debug("Add handlers to new logger.")
    new_logger.addHandler(file_handeler)
    new_logger.addHandler(rich_han)

    logger.info(
        f"New logger has made successfully - name:{name} - instance {new_logger}"
    )
    return new_logger


def make_log_dir() -> bool:
    logger.debug("Make the logs folder")
    LOG_DIR = BASE_DIR / "logs"
    try:
        LOG_DIR.mkdir()
        logger.debug("Logs folder is made successfully - True")
        return True
    except FileExistsError:
        logger.debug(
            "Logs folder had existed before and creation was unsuccessful - False"
        )
        return False
