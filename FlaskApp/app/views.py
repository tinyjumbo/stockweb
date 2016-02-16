from app import app

# this file should works as part of controllers for routes
# if we have more actions later we can have a folder for controllers later but now lets keep it here.
# all routes should go here
@app.route("/")
def index():
    return render_template('index.html')