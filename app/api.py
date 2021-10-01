import socketserver
import socket
import json

from app   import app as api, AppSettingsHandler, socketio
from flask import request

@api.route("/api/version")
def version():
    return {
        "version": AppSettingsHandler.SettingsHandler.get_app_version()
    }