from src.models.Project import Project
from src.common.Database import Database

Database.initialize()
project = Project(
        client = "ClientName2",
        contact = 11100011,
        testers = [
                "tester1",
                "tester2"
        ],
        reference = "xx123",
        startDate = "01-01-2020",
        endDate = "02-01-2020",
        description = "first project for testing",
        scope = [
                "www.example1.com",
                "www.example2.com",
                "127.0.0.1"
        ],
        target = "Client Website",
        reviewers = [
                "manager1",
                "client1",
                "developer1"
        ]

)

#Add
#Database.insert(collection="projects",data=project.json())
#Project.addProject(project)

#find
projects = Project.getProjects()

projects_list = []
for project in projects:
    print(project["client"])
    projects_list.append(project)

print("number of projects is :", len(projects_list))
#Delete
Database.delete_many(collection="projects",query={"client": "ClientName"})
#Project.deleteProject(id="a94d6db398774c3b81b317ded2e6bfa2")

#update
#Database.update_one(collection="projects", obj={"client":"ClientName"}, newObj={"$set":{"client":"Best Corprate"}})
Project.editProject(id="a44bc8d9f39944e1a4d8613f514c2d0b", newObj={"client":"NewClientName"})

#get
#projectx = Project.getProject("8e3b375cfc26465c8ff16face1622110")
#print(projectx)

projects = Project.getProjects()

projects_list = []
for project in projects:
    print(project["client"])
    projects_list.append(project)