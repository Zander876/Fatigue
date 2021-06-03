# Report View
from flask import render_template, redirect, url_for, flash, request, Blueprint
from flask_login import current_user, login_required
from FatigueManagement import db
from FatigueManagement.Models import Report
#from FatigueManagement.Assessment_Report.forms import ReportForm

reports = Blueprint('reports', __name__)
