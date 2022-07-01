from flask import Flask


def create_app() -> Flask:
    app = Flask(__name__)

    from .commands import commands_bl

    app.register_blueprint(commands_bl)

    return app
