from flask import Flask     # https://flask.palletsprojects.com/en/3.0.x/
import logging              # https://docs.python.org/3/library/logging.html
from flask_login import LoginManager
from .user import User

from flask_cors import CORS
logging.basicConfig(level=logging.DEBUG)

def create_app():
    
    # instance_relative_config is used to determine where the conguration files are stored, this is used for the local database files, configuration secrets, instance specific data
    app = Flask(__name__, instance_relative_config=True) 
    app.json.sort_keys = False
    CORS(app, resources={r"/auth": {"origins": "*"}})
    login_manager = LoginManager()
  
    # Configure LoginManager
    login_manager.init_app(app)

    # Call methods on the login_manager instance as needed
    login_manager.login_view = 'auth'

    @login_manager.user_loader
    def load_user(eid):
        # Retrieve user
        return User.get(eid)
    # create end points with from the views
    #views.make_endpoints(app)
    app.config.from_mapping(SECRET_KEY='dev',)
    return app