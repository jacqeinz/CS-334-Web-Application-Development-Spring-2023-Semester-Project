from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

users = {
    "888777": "pass1",
    "777444": "pass2"
}

@app.route("/")
def index():
    return render_template("managerPortalLogin.html")

@app.route("/managerPortalLogin", methods=["POST"])
def login():
    empID = request.form["empID"]
    password = request.form["pwd"]
    if empID in users and users[empID] == password:
        return redirect(url_for("management.html"))
    else:
        error = "Invalid credentials. Please try again."
        return redirect("managerPortalLogin.html")