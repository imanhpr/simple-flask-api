from pathlib import Path
from typing import Final

from flask_sqlalchemy import SQLAlchemy

DB: Final = SQLAlchemy()
BASE_DIR: Final = Path(__file__).parent.parent
