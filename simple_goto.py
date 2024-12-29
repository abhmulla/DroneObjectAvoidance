#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
© Copyright 2015-2016, 3D Robotics.
simple_goto.py: GUIDED mode "simple goto" example (Copter Only)

Demonstrates how to arm and takeoff in Copter and how to navigate to points using Vehicle.simple_goto.

Full documentation is provided at http://python.dronekit.io/examples/simple_goto.html
"""

from __future__ import print_function
import time
from dronekit import connect, VehicleMode, LocationGlobalRelative
import argparse

# Set up option parsing to get connection string
parser = argparse.ArgumentParser(description='Commands vehicle using vehicle.simple_goto.')
parser.add_argument('--connect',
                    help="Vehicle connection target string. Example: udp:172.17.208.1:14550")
args = parser.parse_args()

# Use the provided connection string or default to MAVProxy forwarding
connection_string = args.connect if args.connect else "udp:172.17.208.1:14550"

# Connect to the Vehicle
print('Connecting to vehicle on: %s' % connection_string)
vehicle = connect(connection_string, wait_ready=True, heartbeat_timeout=60)


def arm_and_takeoff(aTargetAltitude):
    """
    Arms vehicle and fly to aTargetAltitude.
    """
    print("Basic pre-arm checks")
    # Don't try to arm until autopilot is ready

    print("Arming motors")
    # Copter should arm in GUIDED mode
    vehicle.mode = VehicleMode("GUIDED")
    vehicle.armed = True

    timeout = time.time() + 60  # 60 seconds timeout
    while not vehicle.armed:
        print(" Waiting for arming...")
        time.sleep(1)
    if not vehicle.armed:
        print("Failed to arm vehicle.")
        return


    # print("Arming motors")
    # # Copter should arm in GUIDED mode
    # vehicle.mode = VehicleMode("GUIDED")
    # vehicle.armed = True

    # Confirm vehicle armed before attempting to take off
    timeout = time.time() + 15  # 30 seconds timeout
    while not vehicle.armed:
        print(" Waiting for arming...")
        time.sleep(1)
    if not vehicle.armed:
        print("Failed to arm vehicle.")
        return

    print("Taking off!")
    vehicle.simple_takeoff(aTargetAltitude)  # Take off to target altitude

    # Wait until the vehicle reaches a safe height before processing the goto
    while True:
        print(" Altitude: ", vehicle.location.global_relative_frame.alt)
        if vehicle.location.global_relative_frame.alt >= aTargetAltitude * 0.95:
            print("Reached target altitude")
            break
        time.sleep(1)



arm_and_takeoff(10)

print("Set default/target airspeed to 3")
vehicle.airspeed = 3

print("Going towards first point for 30 seconds ...")
point1 = LocationGlobalRelative(53.281707, -9.031534, 20)  # Adjusted to be near the home location
vehicle.simple_goto(point1)

# sleep so we can see the change in map
time.sleep(30)

print("Going towards second point for 30 seconds (groundspeed set to 10 m/s) ...")
point2 = LocationGlobalRelative(53.282707, -9.031534, 20)  # Adjusted to be near the home location
vehicle.simple_goto(point2, groundspeed=10)

# sleep so we can see the change in map
time.sleep(30)

print("Returning to Launch")
vehicle.mode = VehicleMode("RTL")

# Close vehicle object before exiting script
print("Close vehicle object")
vehicle.close()
