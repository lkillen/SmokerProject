class Controller:     #Charcoal or Fan? because we used fan.is* earlier

    fan = 'fan'
    temp = 'temp'
    desired_temp = 'desired_temp'
    thing = 'thing'

    def __init__(self, fan, temp, desired_temp, thing):
        self.fan = fan
        self.temp = temp
        self.desired_temp = desired_temp
        self.thing = thing

    def takeTemp(self):
        self.temp = self.thing.temp

    def shouldHeat(self):
        if self.temp < self.desired_temp:
            return True
        else:
            return False

    def shouldCool(self):
        if self.temp > self.desired_temp:
            return True
        else:
            return False

    def turnFanOn(self):
        self.fan.turnOn()

    def turnFanOff(self):
        self.fan.turnOff()

    def makeFanGive(self):
        self.fan.setGiving()

    def makeFanTake(self):
        self.fan.setTaking()

    def execute(self):
        self.takeTemp()
        if  self.shouldHeat():
            self.turnFanOn()
            self.makeFanGive()
        elif self.shouldCool():
            self.turnFanOn()
            self.makeFanTake()
        else:
            self.turnFanOff()
        self.fan.execute()