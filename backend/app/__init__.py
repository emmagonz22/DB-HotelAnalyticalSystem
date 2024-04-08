from flask import Flask     # https://flask.palletsprojects.com/en/3.0.x/
import logging              # https://docs.python.org/3/library/logging.html

logging.basicConfig(level=logging.DEBUG)

def create_app():
    # instance_relative_config is used to determine where the conguration files are stored, this is used for the local database files, configuration secrets, instance specific data
    app = Flask(__name__, instance_relative_config=True) 

  
    # create end points with from the views
    #views.make_endpoints(app)
    
    return app