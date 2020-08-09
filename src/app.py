from src.common.Database import Database
from src.models.User import User
from src.models.Project import Project
from src.models.Vulnerability import Vulnerability
from flask import Flask, render_template, request, session, make_response, send_from_directory

app = Flask(__name__)  # '__main__'
app.secret_key = "jose"

@app.before_first_request
def initialize_database():
    Database.initialize()

@app.route('/')
def home_template():
    return render_template('home.html')

@app.route('/oldhome')
def oldhome_template():
    return render_template('homeold.html')

@app.route('/oldlogin')
def oldhomelogin_template():
    return render_template('loginold.html')


@app.route('/login')
def login_template():
    return render_template('login.html')

@app.route('/projects')
def projects_template():
    #fetch projects from model
    projects = Project.getProjects()
    nos_vulns = Project.getProjectNumbersOfVulnerabilities()
    return render_template('projects.html', projects=zip(projects, nos_vulns))

@app.route('/project')
def project_template():
    return render_template('project.html')

@app.route('/vulnerability')
def vulnerability_template():
    return render_template('vulnerability.html')

@app.route('/register')
def register_template():
    return render_template('register.html')


@app.route('/error')
def error_template():
    return render_template('404.html')


@app.route('/<path:path>')
def send_js(path):
    return send_from_directory('templates', path)

@app.route('/login', methods=['POST'])
def login_user():
    email = request.form['email']
    password = request.form['password']

    if User.login_valid(email, password):
        User.login(email)
        return render_template("profile.html", email=session['email'])
    else:
        session['email'] = None
        return render_template('login.html')



@app.route('/auth/register', methods=['POST'])
def register_user():
    email = request.form['email']
    password = request.form['password']
    firstname = request.form['firstname']
    lastname = request.form['lastname']
    username = request.form['username']

    User.register(email=email, password=password, firstname=firstname, lastname=lastname, username=username)

    return render_template("profile.html", email=session['email'])

@app.route('/addProject', methods=['POST'])
def add_project():
    projectName = request.form['projectName']
    client = request.form['client']
    contact = request.form['contact']
    description = request.form['description']
    target = request.form['target']
    scope = request.form['scope']
    startDate = request.form['startDate']
    endDate = request.form['endDate']
    author = request.form['author']
    testers = request.form['testers']
    reviewers = request.form['reviewers']
    executiveSummary = request.form['executiveSummary']
    conclusion = request.form['conclusion']

    project = Project(projectName=projectName, client=client, contact=contact, description=description, target=target,
                      scope=scope, startDate=startDate, endDate=endDate, author=author, testers=testers, reviewers=reviewers,
                      executiveSummary=executiveSummary, conclusion=conclusion)

    Project.addProject(project)

    return render_template("home.html")


if __name__ == '__main__':
    app.run(port=4995, debug=True)