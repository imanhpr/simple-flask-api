import csv

from flask import Blueprint
from psycopg2.errors import UniqueViolation
from sqlalchemy.exc import IntegrityError

from flask_simple_api.models import Celebrity, Quote

from .constant import BASE_DIR, DB
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


from rich import print


@commands_bl.cli.command("insertdumydata")
def insert_dummy_data():
    with BASE_DIR.joinpath("sample_data.csv").open("r") as file:
        reader = csv.reader(file, delimiter=";")
        quotes = []

        for quote in reader:
            main, translate, celebrity = quote
            celb = Celebrity(name=celebrity)
            DB.session.add(celb)
            try:
                DB.session.commit()
            except (UniqueViolation, IntegrityError):
                DB.session.rollback()
                celb = Celebrity.query.filter_by(name=celebrity).first()
            finally:
                DB.session.rollback()
            quotes.append(Quote(celebrity=celb, text=main, translate=translate))
        DB.session.add_all(quotes)
        DB.session.commit()
