import uuid

from flask import session

from src.common.Database import Database
from src.models.Project import Project

__author__ = 'RivaSecurity'


class User(object):
    def __init__(self, firstname, lastname, username, email, password, _id=None, role="normalUser"):
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.email = email
        self.password = password
        self.role = role
        self._id = uuid.uuid4().hex if _id is None else _id

    @classmethod
    def get_by_email(cls, email):
        data = Database.find_one("users", {"email": email})
        if data is not None:
            return cls(**data)

    @classmethod
    def get_by_id(cls, _id):
        data = Database.find_one("users", {"_id": _id})
        if data is not None:
            return cls(**data)

    @staticmethod
    def login_valid(email, password):
        # Check whether a user's email matches the password they sent us
        user = User.get_by_email(email)
        if user is not None:
            # Check the password
            return user.password == password
        return False

    @classmethod
    def register(cls, username, password, email, firstname, lastname):
        user = cls.get_by_email(email)
        if user is None:
            # User doesn't exist, so we can create it
            new_user = cls(email, password, username, firstname, lastname)
            new_user.save_to_mongo()
            session['email'] = new_user.email
            return True
        else:
            # User exists :(
            return False

    @staticmethod
    def login(user_email):
        # login_valid has already been called
        session['email'] = user_email

    @staticmethod
    def logout():
        session['email'] = None

    def getProjects(self):
        #find projects that this user can view, edit, is author of
        pass
        #return Project.find_by_author_id(self._id)


    def json(self):
        return {
            "email": self.email,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "username": self.username,
            "role": self.role,
            "_id": self._id,
            "password": self.password
        }

    def save_to_mongo(self):
        Database.insert("users", self.json())
#add user
#delete user
#update password
#update email
#change role
