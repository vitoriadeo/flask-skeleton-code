import os
from flask import Flask, render_template
from .config import ProdConfig, DevConfig
import logging


def create_app():
    app = Flask(__name__)

    if os.environ.get('FLASK_DEBUG') == '1':
        app.config.from_object(DevConfig)
    else:
        app.config.from_object(ProdConfig)


    logging.basicConfig(
        level=logging.INFO,
        encoding='utf-8',
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[logging.FileHandler('run.log'), logging.StreamHandler()]
    )

    from app.controllers import routes
    app.register_blueprint(routes.bp)

    def not_found_error(error):
        return render_template('error/404.html'), 404
    
    def internal_error(error):
        return render_template('error/500.html'), 500
    
    app.register_error_handler(404, not_found_error)
    app.register_error_handler(500, internal_error)
    
    return app