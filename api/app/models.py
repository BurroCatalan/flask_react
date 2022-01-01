from app import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash
import base64
from datetime import datetime, timedelta
import os

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    firstName = db.Column(db.String(100), index=False, unique=False)
    lastName = db.Column(db.String(100), index=False, unique=False)
    email = db.Column(db.String(120), index=True, unique=True)
    passwordHash = db.Column(db.String(128))
    token = db.Column(db.String(32), index=True, unique=True)
    token_expiration = db.Column(db.DateTime)
    projectRequests = relationship('ProjectRequest', backref='user', lazy=True)

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.passwordHash, password)

    def get_token(self, expires_in=3600):
        now = datetime.utcnow()
        if self.token and self.token_expiration > now + timedelta(seconds=60):
            return self.token
        self.token = base64.b64encode(os.urandom(24)).decode('utf-8')
        self.token_expiration = now + timedelta(seconds=expires_in)
        db.session.add(self)
        return self.token

    def revoke_token(self):
        self.token_expiration = datetime.utcnow() - timedelta(seconds=1)

    @staticmethod
    def check_token(token):
        user = User.query.filter_by(token=token).first()
        if user is None or user.token_expiration < datetime.utcnow():
            return None
        return user

#@login.user_loader
#def load_user(id):
#    return User.query.get(int(id))

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
