class sensorTemperatura:
    def __init__(self, id_sensor, localizaçao):
        self.id_sensor = id_sensor
        self.localizaçao = localizaçao
        self.temperatura_atual = 0.0
          
    def ler_Temperatura(self, nova_leitura):
        self.temperatura_atual = nova_leitura
        print(f"Sensor {self.id_sensor}: temperatura atualizada para : {self.temperatura_atual}")

sensor_01 = sensorTemperatura("ID-A01", "Motor-Principal")

print(f"Sensor: {sensor_01.id_sensor}, Local: {sensor_01.localizaçao}")
        