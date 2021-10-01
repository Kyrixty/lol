import sys
import json
import time
import os

from app              import app, models, utilities, db, AccountManager, AppSettingsHandler, socketio, emit, send, login
from flask            import render_template, request, redirect, url_for, send_from_directory
from flask_login      import LoginManager, login_required, login_user, logout_user, current_user

login.login_view = "loginPage"
#db.create_all() #Use this if new tables need to be created.

@login.user_loader
def load_user(id):
    return models.User.query.get(int(id))

@app.route("/")
def homePage():
    rootdir = os.path.dirname(__file__).split("\\app")[0]
    if os.path.isfile(rootdir+"/app.db") and os.path.isdir(rootdir+"/migrations"):
        return render_template("index.html")
    else:
        return "Your server is almost fully setup! Read \"DB-MIGRATION-HELP.txt\" for information on how to setup your database."

@app.route("/login")
@app.route("/signin")
def loginPage():
    return render_template("login.html")

@socketio.on("connect")
def connection_test():
    send("test")

@socketio.on("Disconnect")
def client_disconnect():
    pass