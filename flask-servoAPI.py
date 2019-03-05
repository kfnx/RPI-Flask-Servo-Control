#!/usr/bin/python
from flask import Flask, jsonify, abort, request, make_response, url_for, render_template 
from flask_cors import CORS, cross_origin
import sys
import RPi.GPIO as GPIO
import time

app = Flask(__name__, static_url_path = "/static")
cors = CORS(app)

def moveServo(pin,goto):
 GPIO.setmode(GPIO.BOARD)
 GPIO.setup(pin,GPIO.OUT)
 p = GPIO.PWM(pin,50)
 p.start(goto)
 time.sleep(0.05)
 p.stop()
 return "move pin "+str(pin)+" and cycle goto "+str(goto)

@app.route('/api', methods = ['GET'])
def move():
    pin = request.args.get('pin', default = 11, type = int)
    goto = request.args.get('goto', default = 7, type = float)
    return moveServo(pin,float(goto))

#!/usr/bin/python
from flask import Flask, jsonify, abort, request, make_response, url_for, render_template 
from flask_cors import CORS, cross_origin
import sys
import RPi.GPIO as GPIO
import time

app = Flask(__name__, static_url_path = "/static")
cors = CORS(app)

def moveServo(pin,goto):
 GPIO.setmode(GPIO.BOARD)
 GPIO.setup(pin,GPIO.OUT)
 p = GPIO.PWM(pin,50)
 p.start(goto)
 time.sleep(0.05)
 p.stop()
 return "move pin "+str(pin)+" and cycle goto "+str(goto)

@app.route('/api', methods = ['GET'])
def move():
    pin = request.args.get('pin', default = 11, type = int)
    goto = request.args.get('goto', default = 7, type = float)
    return moveServo(pin,float(goto))

@app.route('/', methods = ['GET'])
def index():
    return "siodank";

@app.route('/stats', methods = ['GET'])
def stats():
    return "stats @pi";

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)	