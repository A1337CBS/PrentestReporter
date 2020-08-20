from src.common.Database import Database
from src.models.User import User
from src.models.Project import Project
from src.models.Vulnerability import Vulnerability
from flask import Flask, render_template, request, session, make_response, send_from_directory
import pdfkit
from datetime import date
import json

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
def project_template(projectID=None):
    if projectID is None:
        projectID = request.args.get('proj')
    project = Project.getProject(projectID)
    if (projectID != None):
        vulnerabilities = Vulnerability.getVulnerabilities(projectID)
    else:
        vulnerabilities = None
    return render_template('project.html', project = project, vulnerabilities=vulnerabilities)


@app.route('/deleteProject', methods=['POST'])
def delete_project():
    _id = request.form["project_id"]
    Project.deleteProject(id=_id)
    return projects_template()

@app.route('/viewProject')
def view_project():
    return render_template('project.html')

@app.route('/vulnerability')
def vulnerability_template():
    report_id = request.args.get('proj')
    if request.args.get('vuln') != None:
        vuln_id = request.args.get('vuln')
        vulnerability = Vulnerability.getVulnerability(vuln_id)
    else:
        vuln_id=None
        vulnerability=None
    return render_template('vulnerability.html', vuln_id=vuln_id, vulnerability=vulnerability, report_id=report_id)

@app.route('/deleteVulnerability')
def deleteVulnerability():
    vuln_id = request.args.get('vuln')
    projectID = request.args.get('proj')
    Vulnerability.deleteVulnerability(vuln_id)
    return project_template(projectID=projectID)

@app.route('/register')
def register_template():
    return render_template('register.html')


@app.route('/error')
def error_template():
    return render_template('404.html')


@app.route('/<path:path>')
def send_js(path):
    return send_from_directory('templates', path)

@app.route('/project/vendor/<path:path>')
def send_js_vendor(path):
    return send_from_directory('templates/vendor', path)
@app.route('/project/js/<path:path>')
def send_js_js(path):
    return send_from_directory('templates/js', path)
@app.route('/project/css/<path:path>')
def send_js_css(path):
    return send_from_directory('templates/css', path)


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



@app.route('/project', methods=['POST'])
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
        clientLogoID = request.form['clientLogoIDtext']
        if 'clientLogoID' in request.files:
            image = request.files['clientLogoID']
            if image.filename!='':
                #add picture to DB and get ID
                image_id = Project.addImage(image, image.filename)
                clientLogoID = image.filename

        if request.form['projectID'] !=None: #if project  already exist, dont add it, just edit it
            projectID = request.form['projectID']
            if Project.getProject(projectID) != False:
                project = Project(_id=projectID,projectName=projectName, client=client, contact=contact, author=author, description=description, target=target,
                                      scope=scope, startDate=startDate, endDate=endDate, testers=testers, reviewers=reviewers,
                                      executiveSummary=executiveSummary, conclusion=conclusion, clientLogoID=clientLogoID)
                Project.editProject(projectID, project)
            else: #if project does not exist, add it
                project = Project(projectName=projectName, client=client, contact=contact, description=description,
                                  target=target,
                                  scope=scope, startDate=startDate, endDate=endDate, author=author, testers=testers,
                                  reviewers=reviewers,
                                  executiveSummary=executiveSummary, conclusion=conclusion, clientLogoID=clientLogoID)
                Project.addProject(project)

            return projects_template()



@app.route('/addVulnerability', methods=['POST'])
def add_vulnerability():
    report_id = request.form['report_id']
    name = request.form['name']
    status = request.form['status']
    severity = request.form['severity']
    exploitability = request.form['exploitability']
    poc = request.form['poc']
    description = request.form['description']
    comments = request.form['comments']
    references = request.form['references']
    owaspTop10 = request.form['owaspTop10']
    risk = request.form['risk']
    date = request.form['date']
    remediation = request.form['remediation']
    if request.files['pocImage'] != None:
        image = request.files['pocImage']
        print(image.filename)
        # add picture to DB and get ID
        image_id = Vulnerability.addImage(image, image.filename)
        print(image_id)
        pocImage = image.filename

    else:
        pocImage = None
    vuln_id = request.args.get('vuln')
    print(vuln_id)
    if vuln_id !=None: #if vuln  already exist, dont add it, just edit it
            if Vulnerability.getVulnerability(vuln_id) != False:
                print("edit")
                vulnerability = Vulnerability(_id=vuln_id, report_id=report_id, name=name, status=status, severity=severity,
                                              exploitability=exploitability, poc=poc, description=description,
                                              comments=comments,
                                              references=references, owaspTop10=owaspTop10,
                                              risk=risk, remediation=remediation, pocImage=pocImage, date=date)
                Vulnerability.editVulnerability(vuln_id, vulnerability)
            else: #if vuln does not exist, add it
                print("add")
                vulnerability = Vulnerability(report_id=report_id, name=name, status=status, severity=severity,
                                              exploitability=exploitability, poc=poc, description=description,
                                              comments=comments,
                                              references=references, owaspTop10=owaspTop10,
                                              risk=risk, remediation=remediation, pocImage=pocImage, date=date)

                Vulnerability.addVulnerability(vulnerability)

    return project_template(projectID=report_id)

@app.route('/report')
def get_report():
    project_id = request.args.get("project_id")
    project = Project.getProject(id=project_id)
    vulnerabilities = Vulnerability.getVulnerabilities(report_id=project_id)
    severities = Vulnerability.getVulnerabilitiesSeverities(project_id)
    vulnerabilities1 = Vulnerability.getVulnerabilities(report_id=project_id)
    clientLogo = project["clientLogoID"][0]
    print(clientLogo)

    if vulnerabilities != None:
        return render_template('report.html', project=project, vulnerabilities=vulnerabilities, vulnerabilities1 = vulnerabilities1, severities=severities, filename=clientLogo)
    else:
        return False

@app.route('/DownloadPDF')
def download_report():
    if request.args.get("proj") != None:
        project_id = request.args.get("proj")
        if Project.getProject(project_id) != False:
            project = Project.getProject(project_id)
            options = {
                'page-size': 'A4',
                'margin-top': '0in',
                'margin-right': '0in',
                'margin-bottom': '0.2in',
                'margin-left': '0in',
                'footer-center': '[page] of [topage]'

            }
            url = str(request.url_root)+"/report?project_id="+str(project_id)
            pdf = pdfkit.from_url(url, False, options=options)
            response = make_response(pdf)
            response.headers["Content-Type"] = "application/pdf"
            projectName = str(project['projectName'])
            projectName = projectName.replace(" ","-")
            reportName = projectName+"-Report_"+str(date.today())
            response.headers["Content-Disposition"] = "inline; filename="+reportName+".pdf"
            return response

    else:
        return "Missing project ID"

#get IMage data
@app.route('/files/<filename>')
def getImage(filename):
    return Project.getImage(filename=filename)

#get IMage data
@app.route('/files/')
def getNone():
    return "#"


if __name__ == '__main__':
    app.run(port=4996, debug=True)