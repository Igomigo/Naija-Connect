""" This module contains the custom error pages handlers """

from flask import Blueprint, render_template

errors = Blueprint("errors", __name__)

@errors.app_errorhandler(404)
def error_404(error):
    """ This function renders the 404 error custom page """
    return render_template('errors/404.html'), 404


@errors.app_errorhandler(403)
def error_403(error):
    """ This function renders the 403 error custom page """
    return render_template('errors/403.html'), 403


@errors.app_errorhandler(500)
def error_500(error):
    """ This function renders the 500 error custom page """
    return render_template('errors/500.html'), 500