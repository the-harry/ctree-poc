import serial
import time
import requests
from datetime import datetime

HOST = 'http://localhost:8081'
ENDPOINT = '/ctree/api/v1/record/ctreeSQL/metrics'
URI = HOST + ENDPOINT
BAUD = 9600

class Moisture:

    def __init__(self, port='/dev/ttyACM0'):
        self.port = port
        self.data = ''
        self.sensor = self.connect()

    def connect(self):
        global BAUD
        try:
            self.sensor = serial.Serial(self.port, BAUD)
            print('Conectado com sucesso.\n')
            return self.sensor
        except:
            print('Sem conexão na porta ' + str(self.port) + '.\n')
            return 0

    def getData(self):
        self.connect()
        if(self.sensor != 0):
            self.data = str(self.sensor.readline().decode("utf-8").rstrip())
            self.saveData()
        else:
            time.sleep(10)
            self.getData()

    def saveData(self):
        global URI
        try:
            payload = self.buildPayload()
            res = requests.post(url = URI, data = payload)
            print(res.text)
            print(self.data)
        except Exception as e:
            raise e

    def buildPayload(self):
        {
            "garden": "test_garden_01",
            "sensor": "moisture_01",
            "data": self.data
        }
