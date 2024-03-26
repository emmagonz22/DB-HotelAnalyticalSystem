from app import create_app


app = create_app()

@app.route('/')
def index(): # Temporary index endpoint
    return "<h1>Index page</h1>"

if __name__ == "__main__":
  
    app.run()