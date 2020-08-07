

#user id
#project id
#previlige (read only, write)

import uuid
from src.common.Database import Database
#from src.models.Project import Project

__author__ = 'RivaSecurity'


class Access(object):
    def __init__(self, project_id, user_id, prev, _id=None):
        self.project_id = project_id
        self.user_id = user_id
        self.prev = prev
        self._id = uuid.uuid4().hex if _id is None else _id

#give user access to project (read or write)

#provoke user access to project (remove object)

#check if user has access to project (yes or no)

#check what access user has to project (read or write)