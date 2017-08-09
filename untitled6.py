from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/sema')
def sasa():
    return "adadads"


if __name__ == '__main__':
    app.run()

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))


class Usersz(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))