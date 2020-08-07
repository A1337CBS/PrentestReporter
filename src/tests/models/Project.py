from src.models.Project import Project
from src.common.Database import Database

Database.initialize()
project = Project(
        author = "tester1",
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
print("testing add")
Project.addProject(project) #Working

#find
print("testing find all")
projects = Project.getProjects() #Working

projects_list = []
if projects != None:
    for project in projects:
        print(project["_id"])
        projects_list.append(project)

    print("number of projects is :", len(projects_list))

#Delete
print("testing delete")
#print(Project.deleteProject(id="caf248905e1b49598c7ddb58c2ea06e4")) #working

#update
print("testing edit")
print(Project.editProject(id="c9534e72a12b4227900487640af5af8d", newObj={"client":"NewClientName"}))

#get
print("testing find one")
projectx = Project.getProject("fef85927c1804a8ebbfdaa1a2b149002")
print(projectx)
