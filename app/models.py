import re
import json
import datetime

from app         import db, utilities
from flask_login import UserMixin

class User(UserMixin, db.Model):
    '''
    Used to create, edit, store, and 
    retrieve information about users.
    '''
    __tablename__ = "Users"
    #Account information (username, email, password, etc)
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), index=True, unique=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    salt = db.Column(db.String(64), index=True, unique=True)

    #rsa_public_key = db.Column(db.String(2048), index=True, unique=True)
    #rsa_private_key = db.Column(db.String(2048), index=True, unique=True)

    def __repr__(self):
        return "<User object {}>".format(self.username)
    
    def as_dict(self):
        return {c.name: str(getattr(self, c.name)) for c in self.__table__.columns}
    
    def set_password(self, password):
        salt = utilities.Utility.genRandomString(size=64)
        self.password_hash = utilities.Utility.hash_pass_with_salt(password, salt)
        self.salt = salt
    
    def check_password(self, password):
        salt = self.salt
        password_hash = utilities.Utility.hash_pass_with_salt(password, salt)

        if password_hash==self.password_hash:
            return True
        return False
    
    def check_email(self):
        if re.search('^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$', self.email):
            return True
        return False