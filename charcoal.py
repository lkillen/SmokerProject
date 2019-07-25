class Charcoal          #Name of a class is always capitalized

    maxTemp = 'maxTemp'
    minTemp = 'minTemp'
    temp = 'temp'
    baseTemp = 'baseTemp'
    lifespan = 'lifespan'

    def __init__(self, temp, baseTemp, lifespan):

        self.temp = temp
        self.baseTemp = baseTemp
        self.lifespan = lifespan

    def heat(self):
        self.temp = self.temp + 10

    def cool (self):
         self.temp = self.temp - 10

    def heat_to_baseline (self, fan):
        is_cold = self.temp < self.baseTemp
        is_cooling = fan.isCooling()
        if(is_cold and not is_cooling):
            self.heat()

    def cool_to_baseline (self, fan):
         is_hot = self.temp > self.baseTemp
         is_heating = fan.isHeating()
         if(is_hot and not is_heating):
             self.cool()

    def heat_from_fan(self, fan):
        if(fan.isCooling()):
            self.cool()

    def cool_from_fan(self, fan):
        if(fan.isHeating()):
            self.heat()

    def change_temp(self, fan):
        heat_to_baseline(fan)
        heat_from_fan(fan)
        cool_to_baseline(fan)
        cool_from_fan(fan)