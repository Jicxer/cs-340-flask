import sqlite3
import datetime

ct = datetime.datetime.now()

connection = sqlite3.connect('database.db')

with open('countryclub.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()


# Insertion of test-data
# Follow the syntax and cur.execute will run the query.
# cur.execute("INSERT INTO member (id, title, first_name, last_name, dob, location) VALUES (?, ?, ?, ?, ?, ?)",
#             (0, 'Sir', 'Josh', 'Forg', '2018-10-20', 'local') )

#Insert data for members
cur.execute("INSERT INTO members (title, first_name, last_name, dob, location) VALUES (?, ?, ?, ?, ?)",
            ('Sir', 'Hoe', 'Forg', '2018-10-21', 'Everywhere') )

cur.execute("INSERT INTO members (title, first_name, last_name, dob, location) VALUES (?, ?, ?, ?, ?)",
            ('Sir', 'A', 'A', '2018-10-21', 'There') )

cur.execute("INSERT INTO members (title, first_name, last_name, dob, location) VALUES (?, ?, ?, ?, ?)",
            ('Sir', 'B', 'B', '2018-10-21', 'Here') )


#Insert data for clubs
cur.execute("INSERT INTO clubs (name, address, email, phonenumber) VALUES (?, ?, ?, ?)",
            ('Club Morraco', 'NW 23rd St', 'Morracopart@yahoo.com', '123-456-1234') )

#Insert data for sponsors
cur.execute("INSERT INTO sponsors (name, email, phonenumber) VALUES (?, ?, ?)",
            ('Nididas', 'Nidadas@aol.com', '503-503-5003') )

#Insert data for events
cur.execute("INSERT INTO events (name, location, start_date, end_date, public_or_private) VALUES (?, ?, ?, ?, ?)",
            ('Presidential Joust', 'White House', '2022-5-24', '2022-5-24', 'public') )

cur.execute('DELETE FROM members WHERE first_name = ?', ('Hoe',))
connection.commit()
connection.close()