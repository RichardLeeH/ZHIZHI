# -*- coding: utf-8 -*-
# pylint:disable-msg=W0612

import os

from flask import Flask, g
from flask import send_from_directory

from .extensions import (csrf, cache)

# blueprints

from project.api.view import frontend


__all__ = ('create_app', 'create_celery', )

BLUEPRINTS = (
    frontend,
)


def create_app(config=None, app_name='project', blueprints=None):
    app = Flask(app_name,
                static_folder=os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")), 'static'),
                template_folder="templates"
                )
    app.config.from_object('project.config')
    if config:
        app.config.from_pyfile(config)

    if blueprints is None:
        blueprints = BLUEPRINTS

    blueprints_fabrics(app, blueprints)
    extensions_fabrics(app)
    configure_logging(app)

    # error_pages(app)
    file_page(app)
    return app


def blueprints_fabrics(app, blueprints):
    """Configure blueprints in views."""

    for blueprint in blueprints:
        app.register_blueprint(blueprint)


def extensions_fabrics(app):
    # db.init_app(app)
    # login_manager.init_app(app)
    # migrate.init_app(app, db)
    csrf.init_app(app)
    cache.init_app(app)


def file_page(app):
    @app.route('/wifi/admin/version/<filename>')
    def version_file(filename):
        return send_from_directory(os.path.join(app.config['UPLOAD_FOLDER'], "version"),
                                   filename)

    @app.route('/wifi/admin/pictures/<filename>')
    def pictures_file(filename):
        return send_from_directory(os.path.join(app.config['UPLOAD_FOLDER'], "pictures"),
                                   filename)

    @app.route('/wifi/admin/media/<filename>')
    def media_file(filename):
        return send_from_directory(os.path.join(app.config['UPLOAD_FOLDER'], "media"),
                                   filename)

# def error_pages(app):
#     # HTTP error pages definitions
#
#     @app.errorhandler(403)
#     def forbidden_page(error):
#         return render_template("misc/403.html"), 403
#
#     @app.errorhandler(404)
#     def page_not_found(error):
#         return render_template("misc/404.html"), 404
#
#     @app.errorhandler(405)
#     def method_not_allowed(error):
#         return render_template("misc/405.html"), 404
#
#     @app.errorhandler(500)
#     def server_error_page(error):
#         return render_template("misc/500.html"), 500


def configure_logging(app):
    """Configure file(info) and email(error) logging."""

    if app.debug or app.testing:
        # Skip debug and test mode. Just check standard output.
        return

    import logging
    import logging.handlers

    app.logger.setLevel(logging.INFO)

    info_file_handler = logging.handlers.RotatingFileHandler("run.log")
    info_file_handler.setLevel(logging.INFO)
    info_file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s '
        '[in %(pathname)s:%(lineno)d]')
    )
    app.logger.addHandler(info_file_handler)

    # Testing
    # app.logger.info("testing info.")
    # app.logger.warn("testing warn.")
    # app.logger.error("testing error.")
