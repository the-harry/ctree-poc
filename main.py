#!/usr/bin/python3.6

import time
from moisture import Moisture

sensor = Moisture()
while 1:
    for _ in range(10):
        sensor.getData()
    time.sleep(60)
