class Fan:

    is_on = False
    is_giving = False
    thing = 'thing'

    def __init__(self, is_on, is_giving, thing):
        self.is_on = is_on
        self.is_giving = is_giving
        self.thing = thing


    def isCooling(self):
        if self.is_on and not self.is_giving:
            return True
        else:
            return False

    def isHeating(self):
        if self.is_on and self.is_giving:
            return True
        else:
            return False

    def turnOn(self):
        self.is_on = True

    def turnOff(self):
        self.is_on = False

    def setGiving(self):
        self.is_giving = True

    def setTaking(self):
        self.is_giving = False

    def execute(self):
        if self.is_on and self.is_giving and self.thing.canHeat:
            self.thing.heat()
            self.thing.heat()
        elif self.is_on and not self.is_giving and self.thing.canCool:
            self.thing.cool()
            self.thing.cool()