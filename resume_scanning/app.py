from flask import Flask, request, render_template, flash
import pickle
import os
import process

app = Flask(__name__)
app.secret_key = 'dont tell'


@app.route('/', methods = ['POST', 'GET'])
def hello():
    return render_template("home.html")

# @app.route('/bootstrap')
# def boot():
#     return render_template("learning.html")

@app.route('/logout', methods = ['POST', 'GET'])
def logout():
    return render_template("logout.html")

@app.route('/upload', methods = ['GET', 'POST'])
def upload():
    ab = "upload.html"
    UPLOAD_FOLDER = "C:\\Users\\prasa\\projects\\recruitment_project\\resumes"
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    if request.method == "POST":
        file = request.files["file"]
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
        path = UPLOAD_FOLDER+"\\"+file.filename
        print(file.filename)
        process.read_doc(path)
        #flash('File Uploaded Successfully')
        return render_template(ab, message = "Uploaded Successfully")
    return render_template(ab)

@app.route('/login', methods = ['POST', 'GET'])
def login():
    return render_template("login.html")

@app.route('/admin', methods = ['POST', 'GET'])
def adminpage():
    # return render_template("admin.html")
    a = "admin.html"
    database = {'OdaAdmin':'ODA1234'}
    name1 = request.form['username']
    pwd = request.form['password']
    if name1 not in database:
        return render_template('login.html', info = "Invalid Username")
    else:
        if database[name1]!=pwd:
            return render_template("login.html", info = "Invalid Password")
        else:
            return render_template(a)
            


if __name__ == '__main__':
    app.run(debug=True)








#wsgi_app = app.wsgi_app

# database = {'prasad':'1234', 'parth':'5678'}

# @app.route('/form_login', methods = ['POST', 'GET'])
# def login():
#     a = "home.html"
#     name1 = request.form['username']
#     pwd = request.form['password']
#     if name1 not in database:
#         return render_template('login.html', info = "Invalid Username")
#     else:
#         if database[name1]!=pwd:
#             return render_template("login.html", info = "Invalid Password")
#         else:
#             return render_template(a, name = name1)

    # else:
    #     return render_template("login.html")

# if __name__ == '__main__':
#     import os
#     HOST = os.environ.get('SERVER_HOST', 'localhost')
#     try:
#         PORT = int(os.environ,get('SERVER_PORT', '5555'))
#     except ValueError:
#         PORT = 5555
#     app.run(HOST, PORT)