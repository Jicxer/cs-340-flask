import os
import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort
import datetime
from flask_pymongo import PyMongo
       
            
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


@app.route('/')
def home():
    conn = get_db_connection()
    # posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return render_template("/pages/index.html",homeIsActive=True)

@app.route('/index.html')
def other():
    return redirect("/")


@app.route("/member.html", methods=['GET','POST'])
def member_route():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM members")
    data = cur.fetchall()
    conn.close()
    return render_template("/pages/member.html",homeIsActive=True,data=data)

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