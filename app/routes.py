import os

from app import app, db
from app.models import Cafe  # access to the db.Model Tables
from app.forms import EditForm
from flask import render_template, request, redirect, flash, url_for


# all Flask routes
@app.route("/")
def home():
    print(f"Environment is set to: {app.config['ENV']}")
    all_cafes = db.session.query(Cafe).all()
    # for cafe in all_cafes:
    #     print(f"{cafe.name} is located in {cafe.location}")
    return render_template("index.html", all_cafes=all_cafes)


@app.route("/explore")
def explore():
    all_cafes = db.session.query(Cafe).all()
    return render_template("explore.html", all_cafes=all_cafes)


@app.route("/explore/<name>", methods=['GET', 'POST'])
def cafe(name):
    # Instancing the EditForm
    editform = EditForm()
    selected_cafe = Cafe.query.filter_by(name=name).first()
    location = selected_cafe.location  # store current cafes location
    all_cafes = db.session.query(Cafe).all()  # get all cafes in database
    nearby_cafes = []  # empty list
    for c in all_cafes:  # for each cafe in the database
        if c.name != selected_cafe.name:
            if c.location == location:  # if the location matches, then add it to the list
                nearby_cafes.append(c)

    if request.method == 'GET':
        editform.name.data = selected_cafe.name
        editform.img_link.data = selected_cafe.img_url
        editform.location.data = selected_cafe.location
        if selected_cafe.has_sockets == 1:
            editform.sockets.data = "yes"
        elif selected_cafe.has_sockets == 0:
            editform.sockets.data = "no"

        if selected_cafe.has_wifi == 1:
            editform.wifi.data = "yes"
        elif selected_cafe.has_wifi == 0:
            editform.wifi.data = "no"

        if selected_cafe.has_toilet == 1:
            editform.toilets.data = "yes"
        elif selected_cafe.has_toilet == 0:
            editform.toilets.data = "no"

        editform.seats.data = selected_cafe.seats
        editform.coffee_price.data = selected_cafe.coffee_price

    if editform.validate_on_submit():
        print(f"sockets data: {editform.sockets.data}")
        print(f"toilets data: {editform.toilets.data}")
        print(f"wifi data: {editform.wifi.data}")
        selected_cafe.name = editform.name.data
        selected_cafe.img_url = editform.img_link.data
        selected_cafe.location = editform.location.data
        if editform.sockets.data == "yes":
            selected_cafe.has_sockets = 1
        elif editform.sockets.data == "no":
            selected_cafe.has_sockets = 0

        if editform.toilets.data == "yes":
            selected_cafe.has_toilet = 1
        elif editform.toilets.data == "no":
            selected_cafe.has_toilet = 0

        if editform.wifi.data == "yes":
            selected_cafe.has_wifi = 1
        elif editform.wifi.data == "no":
            selected_cafe.has_wifi = 0
        # selected_cafe.has_sockets = editform.sockets.data
        # selected_cafe.has_toilet = editform.toilets.data
        # selected_cafe.has_wifi = editform.wifi.data
        selected_cafe.seats = editform.seats.data
        selected_cafe.coffee_price = editform.coffee_price.data
        db.session.commit()
        return redirect(url_for('explore'))

    return render_template("cafe.html", cafe=selected_cafe, nearby_cafes=nearby_cafes, form=editform)

@app.route("/delete")
def delete():
    cafe_id = request.args.get('id')
    print(f"Deleted cafe with id: {cafe_id}")
    cafe_selected = Cafe.query.get(cafe_id)
    db.session.delete(cafe_selected)
    db.session.commit()
    return redirect(url_for('explore'))



# RESTFUL Routing Structure
# / - GET Request - home page and shows all cafes
# /explore - GET Request - page shows all cafes
# /explore/name - GET Request - shows that specific cafe in it's own rendered page - view button
# /edit/name - PATCH Request - will update the cafe record - edit button
# /add - POST Request - will add a new cafe to the database - an add button
# /delete/name - DELETE Request - deletes the cafe

# Nearby cafes feature
# when cafe is put into /explore/<name>
# use name to get location
# filter query all cafes using that location
# pass into render template
