import uuid
import datetime
from src.common.Database import Database
from src.models.Vulnerability import Vulnerability

__author__ = 'RivaSecurity'

#add version
#add Ladt Modified Date
#add status

class Project(object):
    def __init__(self, projectName, author, client, clientLogoID, contact, testers, startDate, endDate,
                 description, scope, target, executiveSummary, reviewers, conclusion, _id=None, reference=None):
        self.projectName = projectName
        self.author = author
        self.client = client
        self.clientLogoID = clientLogoID,
        self.contact = contact
        self.testers = testers
        self.reference = reference
        self.startDate = startDate
        self.endDate = endDate
        self.description = description
        self.scope = scope
        self.target = target
        self.executiveSummary = executiveSummary
        self.reviewers = reviewers
        self.conclusion = conclusion
        self._id = uuid.uuid4().hex if _id is None else _id


    @classmethod
    def getProjects(cls):
        projects = Database.find(collection='projects', query={})
        if projects != None:
            return projects
        else:
            return False

    @classmethod
    def getProjectNumbersOfVulnerabilities(cls):
        nos_vulns = []
        projects = Database.find(collection='projects', query={})
        for project in projects:
            no_vulns = Database.find(collection='vulnerabilities', query={'report_id': project["_id"]})
            if no_vulns != None:
                nos_vulns.append(no_vulns.count())

        return nos_vulns



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
            project = Database.update_one(collection='projects', obj=project, newObj={"$set": newObj.json()})
            return True
        else:
            return False

    @classmethod
    def deleteProject(cls, id):
        project = Database.find_one(collection='projects', query={'_id': id})
        if project != None:  # edit if element exists
            Vulnerability.deleteVulnerabilitiesOfProject(report_id=id)
            Database.delete_one(collection='projects', query={"_id": id})
            return True
        else:
            return False

    def addImage(image, filename):
        return Database.saveFile(image=image, filename=filename)

    def getImage(filename):
        return Database.getFileByName(filename=filename)


    def json(self):
        return{
           "_id": self._id,
           "projectName": self.projectName,
           "client": self.client,
            "clientLogoID": self.clientLogoID,
            "author": self.author,
           "contact": self.contact,
            "testers": self.testers,
            "reference": self.reference,
            "startDate": self.startDate,
            "endDate": self.endDate,
            "description": self.description,
            "scope": self.scope,
            "target": self.target,
            "reviewers": self.reviewers,
            "executiveSummary": self.executiveSummary,
            "conclusion": self.conclusion
        }