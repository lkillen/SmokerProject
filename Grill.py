class Grill:

    charcoal = 'charcoal'       # class variable shared by all instances
    meat = 'meat'
    temp = 0
    minTemp = 0

    def __init__(self, a1, a2):           #This is called an initializer
        self.charcoal = a1          # instance variable unique to each instance
        self.meat = a2

    def heat(self):
        self.temp = self.temp + 7
        print('grill heating ' + str(self.temp))


    def cool(self):
        self.temp = self.temp - 7

    def shouldHeat(self):
        if self.temp < self.charcoal.temp:
            return True
        else:
            return False

    def shouldCool(self):
        if self.temp > self.charcoal.temp:
            return True
        else:
            return False

    def execute(self):
        self.charcoal.execute()
        if self.shouldHeat():
            self.heat()
        elif self.shouldCool():
            self.cool()