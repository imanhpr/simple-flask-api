from flask import Flask


def create_app() -> Flask:
    app = Flask(__name__)

    from .commands import commands_bl
    from .urls import urls_bl

    app.register_blueprint(commands_bl)
    app.register_blueprint(urls_bl)

    from .constant import API

    API.init_app(app)

    return app
