#/home/pi/Documents/RpiFlaskServer/run.py
import sys
import Adafruit_DHT
import time
import RPi.GPIO as GPIO
from flask import Flask, render_template

#Creates a Flask web application instance.
app = Flask(__name__)

#This sets up GPIO pin numbering based on the physical pin numbers on the Raspberry Pi board.
GPIO.setmode(GPIO.BOARD)
#This disables GPIO warnings.
GPIO.setwarnings(False)
#he script sets up two GPIO pins,(ledRed and ledbl) as outputs and initializes them to a low state (LEDs off).
ledRed = 32
ledbl = 36
 
# Define led pins as output
GPIO.setup(ledRed, GPIO.OUT)   
GPIO.setup(ledbl, GPIO.OUT) 
 
# Keep LEDs off in the beginning 
GPIO.output(ledRed, GPIO.LOW)
GPIO.output(ledbl, GPIO.LOW)

#Defines a route for the home page (/) that reads sensor data, sets up templateData, 
#and renders an HTML template (index.html).
@app.route("/")
def index():
    # Check the current status of lights in the room
    ledRedSts = GPIO.input(ledRed)
    ledblSts = GPIO.input(ledbl)
         
    # Check the humidity and temperature 
    humidity, temperature = Adafruit_DHT.read_retry(11, 21)
     
    #Store the status and the sensor values in a dictionary called templateData
    templateData = {
            'ledRed'  : ledRedSts,
            'ledbl'  : ledblSts,
            'humidity': humidity
            'temperature' : temperature
        }
    # The data is then passed to the render_template function, which renders the HTML template index.html with the provided data.
    return render_template('index.html', **templateData)

#Defines a route that takes parameters (deviceName and action) and performs actions on the specified device.
@app.route("/<deviceName>/<action>")
# it determines the GPIO pin associated with the specified deviceName (either 'ledRed' or 'ledbl'). 
#Depending on the specified action ('on' or 'off'), it sets the GPIO pin state accordingly.
def action(deviceName, action):
    if deviceName == 'ledRed':
            actuator = ledRed
    if deviceName == 'ledbl':
        actuator = ledbl
    if action == "on":
        GPIO.output(actuator, GPIO.HIGH)
    if action == "off":
        GPIO.output(actuator, GPIO.LOW)
              
    ledRedSts = GPIO.input(ledRed)
    ledblSts = GPIO.input(ledbl)
    
    templateData = {
        'ledRed'  : ledRedSts,
                'ledbl'  : leblSts,
            'humidity': humidity
                'temperature'    : temperature
    }
    return render_template('index.html', **templateData)
 
if __name__ == "__main__":
   app.run(host='0.0.0.0', port=5000, debug=True)
