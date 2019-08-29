class Charcoal:          #Name of a class is always capitalized

    maxTemp = 'maxTemp'
    minTemp = 'minTemp'
    temp = 'temp'
    baseTemp = 'baseTemp'
    lifespan = 'lifespan'

    def __init__(self, temp, baseTemp, lifespan, maxTemp, minTemp):

        self.temp = temp
        self.baseTemp = baseTemp
        self.lifespan = lifespan
        self.maxTemp = maxTemp
        self.minTemp = minTemp

    def heat(self):
        self.temp = self.temp + 10

    def cool (self):
        self.temp = self.temp - 10

    def canHeat(self):
        if self.temp < self.maxTemp:
            return True
        else:
            return False

    def canCool(self):
        if self.temp > self.minTemp:
            return True
        else:
            return False

    def shouldHeatToBaseline(self):
        if self.temp < self.baseTemp:
            return True
        else:
            return False

    def shouldCoolToBaseline(self):
        if self.temp > self.baseTemp:
            return True
        else:
            return False

    def execute(self):
        if self.shouldHeatToBaseline():
            self.heat()
        elif self.shouldCoolToBaseline():
            self.cool()