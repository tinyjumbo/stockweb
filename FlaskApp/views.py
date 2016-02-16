from app import app
# all routes should go here
@app.route("/")
def index():
    return render_template('index.html')