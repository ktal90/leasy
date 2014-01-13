# -*- coding: utf-8 -*-

"""
leasy models.
"""
from flask.ext.sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, \
     check_password_hash

db = SQLAlchemy()

class Property(db.Model):
    
    __tablename__ = 'property'
  
    id = db.Column(db.Integer, primary_key=True)
    property_name = db.Column(db.String, nullable=False)
    
    def __init__(self, unit_name=None):
        self.property_name = property_name
        
    def __repr__(self):
        return '<Property Name "{property_name}">'.format(property_name=self.property_name)

class Unit(db.Model):
  
    __tablename__ = 'unit'
    
    id = db.Column(db.Integer, primary_key=True)
    unit_name = db.Column(db.String, nullable=False)

    
    def __init__(self, unit_name=None):
        self.unit_name = unit_name
        
    def __repr__(self):
        return '<Unit Name "{unit_name}">'.format(unit_name=self.unit_name)

class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String, nullable=False)
    lastname = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    pw_hash = db.Column(db.String, nullable=False)


    def __init__(self, firstname=None, lastname=None, email=None, password=None):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.set_password(password)

    def set_password(self, password):
        self.pw_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.pw_hash, password)

    def __repr__(self):
        return '<User "{firstname}">'.format(firstname=self.firstname)