#this file is used to run your flask-based-database-interacting-website persistently!

#change this line to run the app that you want to run
# from app.db_connector.db_connector import app
#for example, the above line tells to run the sample db connection app in db_connector/ directory
from app.app import app
#from step0.webapp import webapp

#then from the commandline run:
#./venv/bin/activate
#gunicorn run:app -b 0.0.0.0:8842
# gunicorn run:app -b 0.0.0.0:8042 -D 
#eg. gunicorn run:app -b 0.0.0.0:8842