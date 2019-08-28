#!/usr/bin/python3.6
from moisture import Moisture

sensor = Moisture()
while 1:
    sensor.getData()
