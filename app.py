import os
import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect, abort

from werkzeug.exceptions import abort
import datetime
from flask_pymongo import PyMongo

def app(environ, start_response):
    data = b"Hello, World!\n"
    start_response("200 OK", [
        ("Content-Type", "text/plain"),
        ("Content-Length", str(len(data)))
    ])
    return iter([data])
            
app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/"
app.config['SECRET_KEY'] = 'secret'
mongo = PyMongo(app)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn






# Main route for the homepage
@app.route('/')
def home():
    conn = get_db_connection()
    conn.close()
    return render_template("/pages/index.html",homeIsActive=True)

# Return to the index.html route since it was already defined
@app.route('/index.html')
def other():
    return redirect("/")

# ====================================================== Members Functionality ==========================================================
def get_member_id(id):
    conn = get_db_connection()
    entity = conn.execute('SELECT * FROM members WHERE id = ?',
                        (id,)).fetchone()
    conn.close()
    if entity is None:
        abort(404)
    return entity

# Route for members database
@app.route("/member.html", methods=['GET','POST'])
def member_route():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM members")
    data = cur.fetchall()
    conn.close()
    return render_template("/pages/member.html",homeIsActive=True,data=data)

#App route to add members. This is called within the member.html
@app.route("/add-members", methods=['GET','POST'])
def add_members():
        # get the fields data

        if(request.method == "GET"):
            return render_template("/members.html")

        elif (request.method == "POST"):
            title = request.form['title']
            first_name = request.form['first_name']
            last_name = request.form['last_name']
            dob = request.form['dob']
            location = request.form['location']
            conn = get_db_connection()

            if not title:
                flash('Enter a title!')
            elif not first_name:
                flash('Enter a first name!')
            elif not last_name:
                flash('Enter a last_name!')
            elif not dob:
                flash('Enter a dob!')
            elif not location:
                flash('Enter a location!')
            else:
                conn.execute('INSERT INTO members (title, first_name, last_name, dob, location) VALUES (?, ?, ?, ?, ?)',
                                (title, first_name, last_name, dob, location))
            conn.commit()
            conn.close()

            return redirect("/member.html")

@app.route("/update-members", methods=['GET','POST'])
def update_members():
        # get the fields data

        # post = get_member_id(id)

        if (request.method == "POST"):
            id = request.form['id']
            title = request.form['title']
            print(title)
            first_name = request.form['first_name']
            last_name = request.form['last_name']
            dob = request.form['dob']
            location = request.form['location']
            conn = get_db_connection()

            if not title:
                flash('Enter a title!')
            elif not first_name:
                flash('Enter a first name!')
            elif not last_name:
                flash('Enter a last_name!')
            elif not dob:
                flash('Enter a dob!')
            elif not location:
                flash('Enter a location!')
            else:
                conn.execute('UPDATE members SET title = ?, first_name = ?, last_name = ?, dob = ?, location = ?'
                            ' WHERE id = ?',
                            (title, first_name, last_name, dob, location, id))
            conn.commit()
            conn.close()

            return redirect("/member.html")

@app.route('/<int:id>/delete-members', methods=('POST', 'GET'))
def delete_members(id):
    post = get_member_id(id)
    conn = get_db_connection()
    conn.execute('DELETE FROM members WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    flash('"{}" was successfully deleted!'.format(post['title']))
    return redirect("/member.html")

# ====================================================== Clubs Functionality ==========================================================
def get_clubs_id(id):
    conn = get_db_connection()
    entity = conn.execute('SELECT * FROM clubs WHERE id = ?',
                        (id,)).fetchone()
    conn.close()
    if entity is None:
        abort(404)
    return entity

@app.route("/clubs.html", methods=['GET','POST'])
def clubs_route():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM clubs")
    data = cur.fetchall()
    conn.close()
    return render_template("/pages/clubs.html",homeIsActive=True,data=data)

@app.route("/add-clubs", methods=['GET','POST'])
def add_clubs():
        # get the fields data

        if(request.method == "GET"):
            return render_template("/clubs.html")

        elif (request.method == "POST"):
            name = request.form['name']
            address = request.form['address']
            email = request.form['email']
            phonenumber = request.form['phonenumber']
            conn = get_db_connection()

            if not name:
                flash('Enter a club name!')
            elif not address:
                flash('Enter an address!')
            elif not email:
                flash('Enter an email!')
            elif not phonenumber:
                flash('Enter a phone number!')
            else:
                conn.execute('INSERT INTO clubs (name, address, email, phonenumber) VALUES (?, ?, ?, ?)',
                                (name, address, email, phonenumber))
            conn.commit()
            conn.close()

            return redirect("/clubs.html")

@app.route("/update-clubs", methods=['GET','POST'])
def update_clubs():
        # get the fields data

        # post = get_member_id(id)

        if (request.method == "POST"):
            id = request.form['id']
            name = request.form['name']
            address = request.form['address']
            email = request.form['email']
            phonenumber = request.form['phonenumber']
            conn = get_db_connection()

            if not name:
                flash('Enter a club name!')
            elif not address:
                flash('Enter an address!')
            elif not email:
                flash('Enter an email!')
            elif not phonenumber:
                flash('Enter a phone number!')
            else:
                conn.execute('UPDATE clubs SET name = ?, address = ?, email = ?, phonenumber = ?'
                            ' WHERE id = ?',
                            (name, address, email, phonenumber, id))
            conn.commit()
            conn.close()

            return redirect("/clubs.html")

@app.route('/<int:id>/delete-clubs', methods=('POST', 'GET'))
def delete_clubs(id):
    post = get_clubs_id(id)
    print(id)
    conn = get_db_connection()
    conn.execute('DELETE FROM clubs WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    flash('"{}" was successfully deleted!'.format(post['name']))
    return redirect("/clubs.html")

# ====================================================== Sponsors Functionality ==========================================================

@app.route("/sponsors.html", methods=['GET','POST'])
def sponsors_route():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM sponsors")
    data = cur.fetchall()
    conn.close()
    return render_template("/pages/sponsors.html",homeIsActive=True,data=data)

def get_sponsors_id(id):
    conn = get_db_connection()
    entity = conn.execute('SELECT * FROM sponsors WHERE id = ?',
                        (id,)).fetchone()
    conn.close()
    if entity is None:
        abort(404)
    return entity

@app.route("/add-sponsors", methods=['GET','POST'])
def add_sponsors():
        # get the fields data

        if(request.method == "GET"):
            return render_template("/sponsors.html")

        elif (request.method == "POST"):
            service_id = request.form['service_id']
            name = request.form['name']
            email = request.form['email']
            phonenumber = request.form['phonenumber']
            conn = get_db_connection()

            if not service_id:
                flash('Enter a club name!')
            elif not name:
                flash('Enter a name!')
            elif not email:
                flash('Enter an email!')
            elif not phonenumber:
                flash('Enter a phone number!')
            else:
                conn.execute('INSERT INTO sponsors (service_id, name, email, phonenumber) VALUES (?, ?, ?, ?)',
                                (service_id, name, email, phonenumber))
            conn.commit()
            conn.close()

            return redirect("/sponsors.html")

@app.route("/update-sponsors", methods=['GET','POST'])
def update_sponsors():
        # get the fields data

        # post = get_member_id(id)

        if (request.method == "POST"):
            id = request.form['id']
            service_id = request.form['service_id']
            name = request.form['name']
            email = request.form['email']
            phonenumber = request.form['phonenumber']
            conn = get_db_connection()

            if not id:
                flash('Enter an ID!')
            elif not service_id:
                flash('Enter a club name!')
            elif not name:
                flash('Enter an address!')
            elif not email:
                flash('Enter an email!')
            elif not phonenumber:
                flash('Enter a phone number!')
            else:
                conn.execute('UPDATE sponsors SET service_id = ?, name = ?, email = ?, phonenumber = ?'
                            ' WHERE id = ?',
                            (service_id, name, email, phonenumber, id))
            conn.commit()
            conn.close()

            return redirect("/sponsors.html")

@app.route('/<int:id>/delete-sponsors', methods=('POST', 'GET'))
def delete_sponsors(id):
    post = get_sponsors_id(id)
    print(id)
    conn = get_db_connection()
    conn.execute('DELETE FROM sponsors WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    flash('"{}" was successfully deleted!'.format(post['name']))
    return redirect("/sponsors.html")

# ====================================================== Events Functionality ==========================================================

@app.route("/events.html", methods=['GET','POST'])
def events_route():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM events")
    data = cur.fetchall()
    conn.close()
    return render_template("/pages/events.html",homeIsActive=True,data=data)

def get_events_id(id):
    conn = get_db_connection()
    entity = conn.execute('SELECT * FROM events WHERE id = ?',
                        (id,)).fetchone()
    conn.close()
    if entity is None:
        abort(404)
    return entity

@app.route("/add-events", methods=['GET','POST'])
def add_events():
        # get the fields data

        if(request.method == "GET"):
            return render_template("/events.html")

        elif (request.method == "POST"):
            name = request.form['name']
            location = request.form['location']
            start_date = request.form['start_date']
            end_date = request.form['end_date']
            public_or_private = request.form['public_or_private']
            conn = get_db_connection()


            if not name:
                flash('Enter a name!')
            elif not location:
                flash('Enter a location!')
            elif not start_date:
                flash('Enter a start_date!')
            elif not end_date:
                flash('Enter a end_date!')
            elif not public_or_private:
                flash('Enter if event is public or private!')
            else:
                conn.execute('INSERT INTO events (name, location, start_date, end_date, public_or_private) VALUES (?, ?, ?, ?, ?)',
                                (name, location, start_date, end_date, public_or_private))
            conn.commit()
            conn.close()

            return redirect("/events.html")

@app.route("/update-events", methods=['GET','POST'])
def update_events():
        # get the fields data

        # post = get_member_id(id)

        if (request.method == "POST"):
            id = request.form['id']
            name = request.form['name']
            location = request.form['location']
            start_date = request.form['start_date']
            end_date = request.form['end_date']
            public_or_private = request.form['public_or_private']
            conn = get_db_connection()


            if not name:
                flash('Enter a name!')
            elif not location:
                flash('Enter a location!')
            elif not start_date:
                flash('Enter a start_date!')
            elif not end_date:
                flash('Enter a end_date!')
            elif not public_or_private:
                flash('Enter if event is public or private!')
            else:
                conn.execute('UPDATE events SET name = ?, location = ?, start_date = ?, end_date = ?, public_or_private = ?'
                            ' WHERE id = ?',
                            (name, location, start_date, end_date, public_or_private, id))
            conn.commit()
            conn.close()

            return redirect("/events.html")

@app.route('/<int:id>/delete-events', methods=('POST', 'GET'))
def delete_events(id):
    post = get_events_id(id)
    print(id)
    conn = get_db_connection()
    conn.execute('DELETE FROM events WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    flash('"{}" was successfully deleted!'.format(post['name']))
    return redirect("/events.html")





if __name__ == "__main__":
    app.run(debug=True ,port=8080)