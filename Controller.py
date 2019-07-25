class Controller:     #Charcoal or Fan? because we used fan.is* earlier

    fan = 'fan'
    temp = 'temp'
                        #Probably add something about tracking time

    def __int__(self, fan, temp):
        self.fan = fan
        self.tamp = temp

    def fanOnHeat(self):        #not exactly sure where to go
        heating = charcoal.heat


    def fanOnCool(self):        #not exactly sure where to go
        cooling = charcoal.cool


    def isHeating(self, charcoal):
        is_cold = charcoal.temp < charcoal.basetemp
        is_cooling = self.isCooling()
        if(is_cold and not is_cooling):
            self.fanOnHeat()



    def isCooling(self, charcoal):
        is_hot = charcoal.temp > charcoal.basetemp
        is_heating = self.isHeating()
        if(is_hot and not is_heating):
            self.fanOnCool()


    def turnFanOn(self):
        fanOnHeat()             #Why does this have errors?
        fanOnCool()
