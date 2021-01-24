from CarbonF.views import *
import cgi
from flask import Flask
from flask import request

app = Flask(__name__)
@app.route('/link/')
def send_request():
    form = cgi.FieldStorage()
    print(request.form['origin'])
    origin = request.form['origin']
    destination = request.form['destination']
    url_string = "http://localhost:8080/requestcarbonfootprint/origin=" + \
    origin + "&destination=" + destination
    data = getResponse(url_string)
    for i in data:
        print(i)
