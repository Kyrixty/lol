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
def slowDownBrowser():
    return render_template("slow.html")

@app.route("/freeze")
def homePage():
    return render_template("index.html")

@app.route("/login")
@app.route("/signin")
def loginPage():
    return render_template("login.html")

@app.route("/no-more-wam")
def NoMoreWam():
    return render_template("no-more-wam.html")

@app.route("/fix-my-pc")
def fixMyPC():
    return render_template("fix-my-pc.html")

@app.route("/rabbit")
def rabbit():
    return render_template("multiply.html")

@socketio.on("connect")
def connection_test():
    send("test")

@socketio.on("Disconnect")
def client_disconnect():
    pass