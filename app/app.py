
from flask import Flask, render_template, request, url_for, flash, redirect, abort

from werkzeug.exceptions import abort
import datetime
from flask_pymongo import PyMongo
from app.db_connector.db_connect import connect_to_database, execute_query

def app(environ, start_response):
    data = b"Hello, World!\n"
    start_response("200 OK", [
        ("Content-Type", "text/plain"),
        ("Content-Length", str(len(data)))
    ])
    return iter([data])
            
app = Flask(__name__)
app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/"
app.config['SECRET_KEY'] = 'secret'
mongo = PyMongo(app)



# Main route for the homepage
@app.route('/')
def home():
    conn = connect_to_database()
    conn.close()
    return render_template("/pages/index.html",homeIsActive=True)

# Return to the index.html route since it was already defined
@app.route('/index.html')
def other():
    return redirect("/")

# ====================================================== Members Functionality ==========================================================/

# Route for members database
@app.route("/member.html", methods=['GET','POST'])
def member_route():
    conn = connect_to_database()
    cur = conn.cursor()
    cur.execute("SELECT * FROM members")
    data = cur.fetchall()
    conn.close()
    return render_template("/pages/member.html",homeIsActive=True,data=data)

#App route to add members. This is called within the member.html
@app.route("/add-members", methods=['GET','POST'])
def add_members():
    # get the fields data
    conn = connect_to_database()
    if (request.method == "POST"):
        print('reached')
        title = request.form['title']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        dob = request.form['dob']
        location = request.form['location']

        if not title:
            flash('Enter a title!')
            print('No title')
        elif not first_name:
            flash('Enter a first name!')
        elif not last_name:
            flash('Enter a last_name!')
        elif not dob:
            flash('Enter a dob!')
        elif not location:
            flash('Enter a location!')
        else:
            query = ('INSERT INTO members (title, first_name, last_name, dob, location) VALUES (%s,%s,%s,%s,%s)')
            data = (title, first_name, last_name, dob, location)
            execute_query(conn, query, data)
            return redirect("/member.html")
        
    elif(request.method == "GET"):
        return redirect(member_route)

    conn.commit()
    conn.close()
    return redirect("/member.html")

@app.route("/update-members", methods=['GET','POST'])
def update_members():
        # get the fields data

        if (request.method == "POST"):
            id = request.form['id']
            title = request.form['title']
            first_name = request.form['first_name']
            last_name = request.form['last_name']
            dob = request.form['dob']
            location = request.form['location']
            conn = connect_to_database()

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
                query = "UPDATE members SET title = %s, first_name = %s, last_name = %s, dob = %s, location = %s WHERE id = %s"
                data = (title, first_name, last_name, dob, location, id)
                execute_query(conn, query, data)
            conn.commit()
            conn.close()

            return redirect("/member.html")


@app.route('/<int:id>/delete-members', methods=('POST', 'GET'))
def delete_members(id):
    conn = connect_to_database()
    query = "DELETE FROM members WHERE id = %s"
    data = (id,)
    result = execute_query(conn, query, data)
    return redirect("/member.html")


# ====================================================== Clubs Functionality ==========================================================


@app.route("/clubs.html", methods=['GET','POST'])
def clubs_route():
    conn = connect_to_database()
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
            conn = connect_to_database()

            if not name:
                flash('Enter a club name!')
            elif not address:
                flash('Enter an address!')
            elif not email:
                flash('Enter an email!')
            elif not phonenumber:
                flash('Enter a phone number!')
            else:
                query = ('INSERT INTO clubs (name, address, email, phonenumber) VALUES (%s,%s,%s,%s)')
                data = (name, address, email, phonenumber)
                execute_query(conn, query, data)

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
            conn = connect_to_database()

            if not name:
                flash('Enter a club name!')
            elif not address:
                flash('Enter an address!')
            elif not email:
                flash('Enter an email!')
            elif not phonenumber:
                flash('Enter a phone number!')
            else:
                query ="UPDATE clubs SET name = %s, address = %s, email = %s, phonenumber = %s WHERE id = %s"
                data = (name, address, email, phonenumber, id)
                execute_query(conn, query, data)
            conn.commit()
            conn.close()

            return redirect("/clubs.html")


@app.route('/<int:id>/delete-clubs', methods=('POST', 'GET'))
def delete_clubs(id):
    conn = connect_to_database()
    query = "DELETE FROM clubs WHERE id = %s"
    data = (id,)
    result = execute_query(conn, query, data)
    return redirect("/clubs.html")

# ====================================================== Sponsors Functionality ==========================================================

@app.route("/sponsors.html", methods=['GET','POST'])
def sponsors_route():
    conn = connect_to_database()
    cur = conn.cursor()
    cur.execute("SELECT * FROM sponsors")
    data = cur.fetchall()
    conn.close()
    return render_template("/pages/sponsors.html",homeIsActive=True,data=data)


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
            conn = connect_to_database()

            if not service_id:
                flash('Enter a club name!')
            elif not name:
                flash('Enter a name!')
            elif not email:
                flash('Enter an email!')
            elif not phonenumber:
                flash('Enter a phone number!')
            else:
                query = ('INSERT INTO sponsors (service_id, name, email, phonenumber) VALUES (%s,%s,%s,%s)')
                data = (service_id, name, email, phonenumber)
                execute_query(conn, query, data)
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
            conn = connect_to_database()

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
                query ="UPDATE sponsors SET service_id = %s, name = %s, email = %s, phonenumber = %s WHERE id = %s"
                data = (service_id, name, email, phonenumber, id)
                execute_query(conn, query, data)
            conn.commit()
            conn.close()

            return redirect("/sponsors.html")

@app.route('/<int:id>/delete-sponsors', methods=('POST', 'GET'))
def delete_sponsors(id):
    conn = connect_to_database()
    query = "DELETE FROM sponsors WHERE id = %s"
    data = (id,)
    result = execute_query(conn, query, data)
    return redirect("/sponsors.html")

# ====================================================== Events Functionality ==========================================================

@app.route("/events.html", methods=['GET','POST'])
def events_route():
    conn = connect_to_database()
    cur = conn.cursor()
    cur.execute("SELECT * FROM events")
    data = cur.fetchall()
    conn.close()
    return render_template("/pages/events.html",homeIsActive=True,data=data)


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
            conn = connect_to_database()


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
                query = ('INSERT INTO events (name, location, start_date, end_date, public_or_private) VALUES (%s,%s,%s,%s, %s)')
                data =  (name, location, start_date, end_date, public_or_private)
                execute_query(conn, query, data)
                
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
            conn = connect_to_database()


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
                query ='UPDATE events SET name = %s, location = %s, start_date = %s, end_date = %s, public_or_private = %s WHERE id = %s'
                data = (name, location, start_date, end_date, public_or_private, id)
                execute_query(conn, query, data)
            conn.commit()
            conn.close()

            return redirect("/events.html")

@app.route('/<int:id>/delete-events', methods=('POST', 'GET'))
def delete_events(id):
    conn = connect_to_database()
    query = "DELETE FROM events WHERE id = %s"
    data = (id,)
    result = execute_query(conn, query, data)
    return redirect("/events.html")

