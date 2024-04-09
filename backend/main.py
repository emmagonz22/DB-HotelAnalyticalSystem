from app import create_app


app = create_app()

#import .app.routes
from app.routes import *

@app.route('/')
def index(): # Temporary index endpoint
    return "<h1>Index page</h1>"

if __name__ == "__main__":
  
    app.run()