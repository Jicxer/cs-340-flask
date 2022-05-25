import os
import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect
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

# def get_post(post_id):
#     conn = get_db_connection()
#     post = conn.execute('SELECT * FROM posts WHERE id = ?',
#                         (post_id,)).fetchone()
#     conn.close()
#     if post is None:
#         abort(404)
#     return post


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

# Route for members database
@app.route("/member.html", methods=['GET','POST'])
def member_route():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM members")
    data = cur.fetchall()
    conn.close()
    return render_template("/pages/member.html",homeIsActive=True,data=data)

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
            conn.execute('INSERT INTO members (title, first_name, last_name, dob, location) VALUES (?, ?, ?, ?, ?)',
                            (title, first_name, last_name, dob, location))
            conn.commit()
            conn.close()

            return redirect("/member.html")


@app.route("/search-members", methods=['GET','POST'])
def search_members():
        # get the fields data

        if(request.method == "GET"):
            return render_template("/members.html")

        elif (request.method == "POST"):
            title = request.form['title']
            print(title)
            first_name = request.form['first_name']
            last_name = request.form['last_name']
            dob = request.form['dob']
            location = request.form['location']
            conn = get_db_connection()
            conn.execute('UPDATE members SET(title, first_name, last_name, dob, location) VALUES (?, ?, ?, ?, ?)',
                            (title, first_name, last_name, dob, location))
            conn.commit()
            conn.close()

            return redirect("/member.html")


@app.route('/delete-members', methods=['GET','POST'])
def delete_members():

        if(request.method == "GET"):
            return render_template("/members.html")

        elif (request.method == "POST"):
            title = request.form['title']
            first_name = request.form['first_name']
            last_name = request.form['last_name']
            dob = request.form['dob']
            location = request.form['location']
            conn = get_db_connection()
            conn.execute('INSERT INTO members (title, first_name, last_name, dob, location) VALUES (?, ?, ?, ?, ?)',
                            (title, first_name, last_name, dob, location))
            conn.commit()
            conn.close()

            return redirect("/member.html")


@app.route("/clubs.html", methods=['GET','POST'])
def clubs_route():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM clubs")
    data = cur.fetchall()
    conn.close()
    return render_template("/pages/clubs.html",homeIsActive=True,data=data)

@app.route("/sponsors.html", methods=['GET','POST'])
def sponsors_route():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM sponsors")
    data = cur.fetchall()
    conn.close()
    return render_template("/pages/sponsors.html",homeIsActive=True,data=data)

@app.route("/events.html", methods=['GET','POST'])
def events_route():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM events")
    data = cur.fetchall()
    conn.close()
    return render_template("/pages/events.html",homeIsActive=True,data=data)


if __name__ == "__main__":
    app.run(debug=True ,port=8080)