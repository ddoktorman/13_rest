from flask import Flask, render_template
import urllib2
import json


response = urllib2.urlopen('https://api.nasa.gov/planetary/apod?api_key=H8p6sviuT0l8EQ5IrshOlRWy1ArBuauYskuhQ4lG')
data_dict = json.loads(response.read())

my_app = Flask(__name__)

@my_app.route('/')
def root():
    return render_template('rest.html', img = data_dict["url"], explained = data_dict["explanation"])

if __name__ == '__main__':
    my_app.debug = True
    my_app.run()
