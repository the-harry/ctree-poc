import serial
import time

class Moisture:
    def __init__(self, port='/dev/ttyACM1'):
        self.port = port
        self.data = ''
        self.baud = 9600
        self.sensor = self.connect()

    def connect(self):
        try:
            self.sensor = serial.Serial(self.port, self.baud)
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
        #TODO SAVE CTREE
        print(self.data)


# payload = {
#     jardim: 1,
#     sensor: 1,
#     metrica: data
# }
