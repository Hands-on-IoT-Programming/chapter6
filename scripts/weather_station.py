#!/usr/bin/env python
from sense_hat import SenseHat
from time import sleep

sense = SenseHat()


data = {}

while True:
    data['temperature'] = sense.get_temperature()
    data['pressure']    = sense.get_pressure()
    data['humidity']    = sense.get_humidity()

    #r = requests.post(thingsboard_url, data=json.dumps(data))
    print(str(data))
    sleep(5)