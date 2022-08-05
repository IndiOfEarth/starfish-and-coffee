import os

from app import app, db
from app.models import Cafe  # access to the db.Model Tables
from flask import render_template


# all Flask routes
@app.route("/")
def home():
    print(f"Environment is set to: {app.config['ENV']}")
    all_cafes = db.session.query(Cafe).all()
    for cafe in all_cafes:
        print(f"{cafe.name} is located in {cafe.location}")
    return render_template("index.html", all_cafes=all_cafes)

@app.route("/explore")
def explore():
    all_cafes = db.session.query(Cafe).all()
    return render_template("explore.html", all_cafes=all_cafes)



# View, add and delete cafes
    # Have buttons underneath each cafeblock - view, edit, delete

# Start by setting up db

# RESTFUL Routing Structure
# / - GET Request - home page and shows all cafes
# /explore - GET Request - page shows all cafes
# /explore/name - GET Request - shows that specific cafe in it's own rendered page - view button
# /edit/name - PATCH Request - will update the cafe record - edit button
# /add - POST Request - will add a new cafe to the database - an add button
# /delete/name - DELETE Request - deletes the cafe