from operator import index
from flask import Blueprint, blueprints

posts=Blueprint('posts',__name__)

@posts.route('/')
def index():

    return '<h1>Welcome to Hompage</h1>'


