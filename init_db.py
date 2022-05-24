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

cur.execute("INSERT INTO members (title, first_name, last_name, dob, location) VALUES (?, ?, ?, ?, ?)",
            ('Sir', 'Hoe', 'Forg', '2018-10-21', 'Everywhere') )

cur.execute("INSERT INTO members (title, first_name, last_name, dob, location) VALUES (?, ?, ?, ?, ?)",
            ('Sir', 'A', 'A', '2018-10-21', 'There') )

cur.execute("INSERT INTO members (title, first_name, last_name, dob, location) VALUES (?, ?, ?, ?, ?)",
            ('Sir', 'B', 'B', '2018-10-21', 'Here') )

connection.commit()
connection.close()