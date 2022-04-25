from email import message

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import psycopg2
from sqlalchemy import Column
from geoalchemy2 import Geometry 
from geoalchemy2 import shape
from shapely.geometry import Point
from datetime import datetime
from geoalchemy2 import func
from flask import Blueprint
from flask_moment import Moment


posts = Flask(__name__)
posts.config['SQLALCHEMY_DATABASE_URI']=True
posts.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:Nehal218@localhost/twitter'

db=SQLAlchemy(posts)
moment = Moment(posts)
class Witer(db.Model):
  __tablename__='Twitter'
  id=db.Column(db.Integer,primary_key=True)
  message=db.Column(db.String(200))
  geom = db.Column(Geometry('POINT'))
  created_at = db.Column(db.DateTime,nullable=False, unique=False, index=False,default=datetime.utcnow)
 

  def __init__(self,message,geo):
    self.message=message
    self.geom = geo
    

    


@posts.route('/')
def index():
  return render_template('index.html')

@posts.route('/submit', methods=['POST'])
def submit():
    if request.method=='POST':
        message= request.form['message']
        lon=request.form['lon']
        lat=request.form['lat']
        geo = 'POINT({} {})'.format(lon, lat)
        witer=Witer(message=message,geo=geo)
        db.session.add(witer)
        db.session.commit()
    
    return render_template('sucess.html')

@posts.route('/fetch')
@posts.route('/fetch/<int:page_num>')
def fetch(page_num ):
 
  posts = Witer.query.paginate(per_page=10, page=page_num, error_out=True)
  return render_template('result.html',posts=posts)


if __name__ == '__main__':  #python interpreter assigns "__main__" to the file you run
  posts.run(debug=True)

