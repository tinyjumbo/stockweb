from app import app

@app.route("/")
# actually should be separated into 3 files routes.py __init__.py and run_server.py
def index():
    return render_template('index.html')