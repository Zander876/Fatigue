from flask import Blueprint, render_template

error_pages = Blueprint('error_pages', __name__)

@error_pages.app_errorhandler(404) #tells it the code for the erro that triggers the pages based on the error handler app
def error_404(error):
    return render_template('error_pages/404.html'), 404 #use tuple when rendering erro templates with the erro code as the last value

@error_pages.app_errorhandler(403) #tells it the code for the erro r that triggers the pages
def error_403(error):
    return render_template('error_pages/403.html'), 403
