from app import app
from flask import render_template
from flask_sqlalchemy import SQLAlchemy

# all Flask routes
@app.route("/")
def home():
    print(f"Environment is set to: {app.config['ENV']}")
    return render_template("index.html")