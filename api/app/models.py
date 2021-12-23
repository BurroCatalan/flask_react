from app import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
#import json

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    first_name = db.Column(db.String(100), index=False, unique=False)
    last_name = db.Column(db.String(100), index=False, unique=False)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)

    #def toJSON(self):
#	return json.dumps(self, default=lambda o: o.__d sort_keys=True, indent=4)


class ProjectRequest(db.Model):
    project_request_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), index=False, unique=False)
    customer_id = relationship("Customer")
    project_type = relationship("Project_Type")
    creator = relationship("User")
    status = relationship("Status")

    def __repr__(self):
        return '<ProjectRequest {}>'.format(self.project_request_id)

class ProjectType(db.Model):
    project_type_id = db.Column(db.Integer, primary_key=True)
    abbreviation = db.Column(db.String(5), index=False, unique=True)
    description = db.Column(db.String(50), index=False, unique=False)

    def __repr__(self):
        return '<ProjectType {}>'.format(self.abbreviation)

class Customer(db.Model):
    customer_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), index=False, unique=True)

    def __repr__(self):
        return '<ProjectType {}>'.format(self.name)

class Status(db.Model):
    status_id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(50), index=False, unique=True)

    def __repr__(self):
        return '<ProjectType {}>'.format(self.description)

class StatusNet(db.Model):
    status_net_id = db.Column(db.Integer, primary_key=True)
    status_id = relationship("Status")
    predecessor_status_id = relationship("Status")

    def __repr__(self):
        return '<ProjectType {}>'.format(self.description)
