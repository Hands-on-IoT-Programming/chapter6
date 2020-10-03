#!/bin/bash
export DBUS_SYSTEM_BUS_ADDRESS=unix:path=/host/run/dbus/system_bus_socket

echo "Watch the rainbow for 5 seconds to check I'm alive..."
# Scripts in this folder run with Python3
./scripts/rainbow.py &

# Move the joystick so that the menu is visualized in the LED matrix
echo "You can always read any of temperature, pressure or humidity with sensor_menu.py, using the Sense Hat josytick"
./scripts/sensor_menu.py &

# joystick_events.py shows the movable pixel on exiting sensor_menu.py
echo "Move the joystick to test I'm still alive..."
./scripts/joystick_events.py &

echo "In parallel watch the environment conditions in the container's log..."
# This script as well as those in ./astropi run with Python (current default in container image is Python2.7)
./scripts/weather_station.py