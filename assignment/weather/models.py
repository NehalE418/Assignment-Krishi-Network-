from email import message
import re
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import psycopg2
import requests
from flask import Blueprint

weather=Flask(__name__)

@weather.route('/')
def index():
  return render_template('index.html')

@weather.route('/cheak', methods=['POST'])
def weathe():
    
    lon=request.form['lon']
    lat=request.form['lat']

    APIkey = "007b02d728cc541066e524d78c1fe633"
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&weatherid={APIkey}"
    # querystring = {"lat": 27.2046, "lon": 77.4977, "APIkey": '007b02d728cc541066e524d78c1fe633'}
    

    # response = requests.request("GET", url, params=querystring )
    r = requests.get(url).json()
    return f'{r}'

if __name__=="__main__":
  weather.run()