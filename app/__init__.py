#Setup app
import os
from app import AppSettingsHandler

from flask            import Flask
from config           import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate    import Migrate
from flask_login      import LoginManager
from flask_socketio   import SocketIO, emit, send

app = Flask(__name__, template_folder=os.path.dirname(__file__)+"/Templates", static_folder=os.path.dirname(__file__)+"/static")
app.config.from_object(Config)
db = SQLAlchemy(app)
login = LoginManager(app)
migrate = Migrate(app, db)
socketio = SocketIO(app)
app.secret_key = AppSettingsHandler.SettingsHandler.get_secret_key()
app.config["Downloadable-files"] = os.path.dirname(__file__)+"/downloadable-files"

from app import views
from app import api