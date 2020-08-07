import pymongo

uri = "mongodb://127.0.0.1:27017"

client = pymongo.MongoClient(uri)
database = client['PentestReporter']#name of db
collection = database['projects']
projects = collection.find({})

print(projects)
project_list =[]

for project in projects:
    project_list.append(project)

print(project_list)
print(project_list[0]["client"])