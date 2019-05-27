from flask import Flask, Blueprint

admin_blu = Blueprint('admin',__name__)

from . import views