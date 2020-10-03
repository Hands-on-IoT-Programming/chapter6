#!/usr/bin/env python
from sense_hat import SenseHat
from time import sleep

sense = SenseHat()


data = {}
timeUpdate = 5
# Workflow execution starts
print ("--- FOURTH TEST: Show the TEMPERATURE/HUMMIDITY/PRESSURE every ", timeUpdate, " seconds")
print ("This is an infinite loop that runs concurrently with THIRD TEST (move dot with the joystick)")

# Workflow execution starts (infinite loop)
sleep(2)
while True:
    data['temperature'] = sense.get_temperature()
    data['pressure']    = sense.get_pressure()
    data['humidity']    = sense.get_humidity()

    #r = requests.post(thingsboard_url, data=json.dumps(data))
    print(str(data))
    sleep(timeUpdate)