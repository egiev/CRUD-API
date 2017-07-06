import os
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

import os
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'db/app.db')

app = Flask(__name__)

CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI

db = SQLAlchemy(app)

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  firstname = db.Column(db.String(80))
  lastname = db.Column(db.String(80))


  def to_dict(self):
    return {
      "id": self.id,
      "firstname": self.firstname,
      "lastname": self.lastname
    }

  def __repr__(self):
    return "<User %r %r %r>" % (self.id, self.firstname, self.lastname)

@app.route('/users/', methods=['GET', 'POST'])
def users():
    if request.method == 'GET':
        users = User.query.all()
    if request.method == 'POST':
        data = request.json
        user = User(**data)
        db.session.add(user)
        db.session.commit()
        users = User.query.all()
    return jsonify({'data': [u.to_dict() for u in users]})

@app.route('/users/<id>/', methods=['GET', 'DELETE', 'PUT'])
def user(id):
    if request.method == 'GET':
      user = User.query.filter_by(id=id).first().to_dict()
      return jsonify({ 'data': user})

    if request.method == 'DELETE':
      user = User.query.filter_by(id=id).first()
      db.session.delete(user)
      db.session.commit()
      users = User.query.all()
      return jsonify({'data': [u.to_dict() for u in users]})

    if request.method == 'PUT':
      user = User.query.get(id)
      user.firstname = request.json.get('firstname')
      user.lastname = request.json.get('lastname')
      db.session.commit()
      users = User.query.all()
      return jsonify({ 'data': [u.to_dict() for u in users]})