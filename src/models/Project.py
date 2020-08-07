import uuid
import datetime
from src.common.Database import Database
#from src.models.Project import Project

__author__ = 'RivaSecurity'


class Project(object):
    def __init__(self, author, client, contact, testers, reference, startDate, endDate, description, scope, target, reviewers, _id=None):
        self.author = author
        self.client = client
        self.contact = contact
        self.testers = testers
        self.reference = reference
        self.startDate = startDate
        self.endDate = endDate
        self.description = description
        self.scope = scope
        self.target = target
        self.reviewers = reviewers
        self._id = uuid.uuid4().hex if _id is None else _id


    @classmethod
    def getProjects(cls):
        projects = Database.find(collection='projects', query={})
        if projects != None:
            return projects
        else:
            return False

    @classmethod
    def getProject(cls, id):
        project = Database.find_one(collection='projects', query={'_id': id})
        if project != None:
            return project
        else:
            return False


    #gets the data from json function and puts it in db
    def addProject(self):
        Database.insert(collection='projects',
                        data=self.json())

    @classmethod
    def editProject(cls, id, newObj):
        project = Database.find_one(collection='projects', query={'_id': id})
        print(project)
        if project != None:  # edit if element exists
            project = Database.update_one(collection='projects', obj=project, newObj={"$set": newObj})
            return True
        else:
            return False

    @classmethod
    def deleteProject(cls, id):
        project = Database.find_one(collection='projects', query={'_id': id})
        if project != None:  # edit if element exists
            print(Database.delete_one(collection='projects', query={"_id": id}))
            return True
        else:
            return False


    def json(self):
        return{
           "_id": self._id,
           "client": self.client,
           "contact": self.contact,
            "testers": self.testers,
            "reference": self.reference,
            "startDate": self.startDate,
            "endDate": self.endDate,
            "description": self.description,
            "scope": self.scope,
            "target": self.target,
            "reviewers": self.reviewers,
        }