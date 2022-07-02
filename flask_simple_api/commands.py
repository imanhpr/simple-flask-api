from flask import Blueprint, current_app
from .constant import DB
from .loggerfactory import logger_factory, make_log_dir

commands_bl = Blueprint("commands", __name__)

logger = logger_factory(__name__)

@commands_bl.cli.command("logdir")
def log_dir_command():
    """Create the logs directory"""
    make_log_dir()

@commands_bl.cli.command("createtables")
def create_tables():
    """Creating models in database"""
    logger.info("Tables has been created.")
    DB.create_all()