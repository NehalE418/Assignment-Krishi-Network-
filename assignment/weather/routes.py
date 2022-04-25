from operator import index
from flask import Blueprint, blueprints

weather=Blueprint('weather',__name__, url_prefix='/weather')

@weather.route('/getdata')
def index():

    return {'key': 'value'}


