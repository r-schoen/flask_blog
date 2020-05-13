import os
from blog.api.utils.misc import get_about

from flask import Flask

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping( # TODO: seperate out
        SECRET_KEY='dev'
        # TODO:  Add configuration to local postgres database
    )

    if test_config is None:
        app.config.from_pyfile('config.py',silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route("/about")
    def about():
        return get_about()

    return app