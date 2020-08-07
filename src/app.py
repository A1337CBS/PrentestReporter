from src.common.Database import Database
from flask import Flask, render_template, request, session, make_response, send_from_directory

app = Flask(__name__)  # '__main__'
app.secret_key = "jose"

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
    return render_template('projects.html')

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

if __name__ == '__main__':
    app.run(port=4995, debug=True)