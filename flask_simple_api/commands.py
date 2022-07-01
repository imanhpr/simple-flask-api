from flask import Blueprint

from .loggerfactory import make_log_dir

commands_bl = Blueprint("commands", __name__)


@commands_bl.cli.command("logdir")
def log_dir_command():
    """Create the logs directory"""
    make_log_dir()
