import os
import psycopg2
from flask import Flask, render_template
from flask import Blueprint

from posts.app2 import posts
from weather.models import weather

app = Flask(__name__)




@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':  
  app.run(debug=True)