# CORE/viewws
from FatigueManagement.Models import Report
from flask import render_template, request, Blueprint
core = Blueprint('core', __name__)

#### Create the CORE pages ###

@core.route('/')
def index():
    return render_template('index.html')

@core.route("/info")
def info():
    return render_template('info.html')
