import logging as lg

from rich.logging import RichHandler

from .constant import BASE_DIR


def logger_factory(name: str) -> lg.Logger:
    new_logger = lg.getLogger(name)

    rich_han = RichHandler()
    file_handeler = lg.FileHandler(BASE_DIR / "logs" / f"{name}.log")

    formaterr = lg.Formatter(
        "%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(message)s"
    )

    rich_han.setLevel(lg.DEBUG)
    file_handeler.setLevel(lg.DEBUG)
    new_logger.setLevel(lg.DEBUG)

    rich_han.setFormatter(formaterr)
    file_handeler.setFormatter(formaterr)

    new_logger.addHandler(file_handeler)
    new_logger.addHandler(rich_han)

    return new_logger


def make_log_dir() -> bool:
    LOG_DIR = BASE_DIR / "logs"
    try:
        LOG_DIR.mkdir()
        return True
    except FileExistsError:
        print("Logs folder had existed before and creation was unsuccessful - False")
    return False
