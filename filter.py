#!/usr/bin/python3.6

import requests

# rodar cron */10 * * * *
HOST = 'http://localhost:8081'
ENDPOINT = '/ctree/api/v1/record/ctreeSQL/metrics'
URI = HOST + ENDPOINT

class Filter:
    def loadData(self):
        global URI
        data = []
        for x in range(10):
            try:
                res = requests.get(URI + (x + 1))
                data.append(res.text)
            except Exception as e:
                break
        return data

    def processData(self, data):
        for x in range(data):
            if (data[x] > 0 & data[x] < 600):
                print('Status: Solo umido')
            elif (data[x] > 600 & data[x] < 950):
                print('Status: Umidade moderada')
            elif (data[x] > 950 & data[x] < 1024):
                print('Status: Solo seco')
            else:
                print('error')

    def filter(self):
        data = self.loadData().sort[-1]
        self.processData(data)

if __name__ == "__main__":
    Filter.filter()
