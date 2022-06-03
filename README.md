# cs-340-flask
Python flask implementation

To activate coding enviroment:

source venv/bin/activate

source ./venv/bin/activate
export FLASK_APP=run.py
python -m flask run -h 0.0.0.0 -p 8042 --reload

Code and html based off flask and python tutorials included below:

Building a Python Note Application Using Flask and MongoDB
https://www.section.io/engineering-education/building-a-simple-python-note-app-with-flask-and-mongodb/

How To Make a Web Application Using Flask in Python 3
https://www.digitalocean.com/community/tutorials/how-to-make-a-web-application-using-flask-in-python-3

https://github.com/knightsamar/CS340_starter_flask_app

How to run persistently:
gunicorn run:webapp -b 0.0.0.0:8020 -D 
