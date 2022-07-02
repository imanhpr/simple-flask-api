from flask import Flask


def create_app() -> Flask:
    app = Flask(__name__)
    app.config[
        "SQLALCHEMY_DATABASE_URI"
    ] = "postgresql://postgres:testpass@postgres_db/api_db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
    app.config["BUNDLE_ERRORS"] = True

    from .commands import commands_bl
    from .models import models_bl
    from .urls import urls_bl

    app.register_blueprint(models_bl)
    app.register_blueprint(commands_bl)
    app.register_blueprint(urls_bl)

    from .constant import API, DB

    DB.init_app(app)
    API.init_app(app)

    return app
