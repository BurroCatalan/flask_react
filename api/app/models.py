from app import db, login
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from itsdangerous import (TimedJSONWebSignatureSerializer
                          as Serializer, BadSignature, SignatureExpired)

#import json

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    firstName = db.Column(db.String(100), index=False, unique=False)
    lastName = db.Column(db.String(100), index=False, unique=False)
    email = db.Column(db.String(120), index=True, unique=True)
    passwordHash = db.Column(db.String(128))
    projectRequests = relationship('ProjectRequest', backref='user', lazy=True)

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def generate_auth_token(self, expiration = 600):
        s = Serializer(app.config['SECRET_KEY'], expires_in = expiration)
        return s.dumps({ 'id': self.id })
    
    @staticmethod
    def verify_auth_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except SignatureExpired:
            return None # valid token, but expired
        except BadSignature:
            return None # invalid token
        user = User.query.get(data['id'])
        return user

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

    #def toJSON(self):
#	return json.dumps(self, default=lambda o: o.__d sort_keys=True, indent=4)


class ProjectRequest(db.Model):
    project_request_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), index=False, unique=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.customer_id'))
    project_type_id =db.Column(db.Integer, db.ForeignKey('project_type.project_type_id'))
    creator_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    status_id = db.Column(db.Integer, db.ForeignKey('status.status_id'))
    status = relationship("Status", backref='project_requests', lazy=True)


    def __repr__(self):
        return '<ProjectRequest {}>'.format(self.project_request_id)

class ProjectType(db.Model):
    project_type_id = db.Column(db.Integer, primary_key=True)
    abbreviation = db.Column(db.String(5), index=False, unique=True)
    description = db.Column(db.String(50), index=False, unique=False)
    projectRequests = relationship('ProjectRequest', backref='project_type', lazy=True)

    def __repr__(self):
        return '<ProjectType {}>'.format(self.abbreviation)

class Customer(db.Model):
    customer_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), index=False, unique=True)
    projectRequests = relationship('ProjectRequest', backref='customer', lazy=True)

    def __repr__(self):
        return '<ProjectType {}>'.format(self.name)

class Status(db.Model):
    status_id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(50), index=False, unique=True)
    

    def __repr__(self):
        return '<ProjectType {}>'.format(self.description)

class StatusNet(db.Model):
    status_net_id = db.Column(db.Integer, primary_key=True)
    status_id = db.Column(db.Integer, db.ForeignKey('status.status_id'))
    predecessor_status_id = db.Column(db.Integer, db.ForeignKey('status.status_id'))

    statusNetStatuus = relationship('Status', foreign_keys=[status_id], lazy=True)
    statusNetPredecessors = relationship('Status', foreign_keys=[predecessor_status_id], lazy=True)


    def __repr__(self):
        return '<ProjectType {}>'.format(self.description)
