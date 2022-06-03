import sqlite3
import datetime

from flask import Flask
from db_connector.db_connect import connect_to_database, execute_query

app = Flask(__name__)



app.run(debug=True)


conn = connect_to_database()

with open('countryclub.sql') as f:
    conn.executescript(f.read())




# Insertion of test-data


#Insert data for members
def insert_members():
    title = 'VIP'
    first_name = 'John' 
    last_name = 'Smith'
    dob = '2018-04-21'
    location = 'White Country Club'
    query = ('INSERT INTO members (title, first_name, last_name, dob, location) VALUES (%s,%s,%s,%s,%s)')
    data = (title, first_name, last_name, dob, location)
    execute_query(conn, query, data)

def update_members():
    title = 'VIP'
    first_name = 'John' 
    last_name = 'Smith'
    dob = '2018-04-21'
    location = 'White Country Club'
    query = "UPDATE members SET title = %s, first_name = %s, last_name = %s, dob = %s, location = %s WHERE id = %s"
    data = (title, first_name, last_name, dob, location, id)
    execute_query(conn, query, data)

#Insert data for clubs
def insert_clubs():
    
    name = 'Club Folk'
    address = '22222 South'
    email = 'Folks@gmail.com'
    phonenumber = '234-234-2234'
    query = ('INSERT INTO clubs (name, address, email, phonenumber) VALUES (%s,%s,%s,%s)')
    data = (name, address, email, phonenumber)
    execute_query(conn, query, data)

#Insert data for sponsors
def insert_sponsors():
    service_id = '2'
    name = 'Adkie'
    email = 'Adike@yahoo.com'
    phonenumber = '123-456-7890'
    query = ('INSERT INTO sponsors (service_id, name, email, phonenumber) VALUES (%s,%s,%s,%s)')
    data = (service_id, name, email, phonenumber)
    execute_query(conn, query, data)

#Insert data for events
def insert_events():
    name = 'Jo Birth'
    location = "Jo's"
    start_date = '2020-04-20'
    end_date = '2020-04-21'
    public_or_private = 'Private'
    query = ('INSERT INTO events (name, location, start_date, end_date, public_or_private) VALUES (%s,%s,%s,%s, %s)')
    data =  (name, location, start_date, end_date, public_or_private)
    execute_query(conn, query, data)


conn.commit()
conn.close()