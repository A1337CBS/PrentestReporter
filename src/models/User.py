import uuid
from src.common.Database import Database
#from src.models.Project import Project

__author__ = 'RivaSecurity'


class User(object):
    def __init__(self, firstname, lastname, username, role, email, password,_id=None):
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.email = email
        self.password = password
        self.role = role
        self._id = uuid.uuid4().hex if _id is None else _id


#add user
#delete user
#update password
#update email
#change role
