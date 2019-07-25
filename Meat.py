class Meat

    type = 'type'
    temp = 'temp'
    cooked = 'cooked'
    time = "time"
    cookTime = cook_Time

    def __int__(self, type, temp, cooked):
        self.type = type
        self.temp = temp
        self.cooked = temp

    def howLong(self):
        print('How long would you like to smoke your food?')
        cook_Time = input()


    def cookTemp(self, Controller):
        #This is the temperature we would like to controller.temp probe to stay at


    def timePassed(self):
        #This would start a timer once the controller.temp reaches the cookTemp

    def desiredTemp(self, Controller):
        #checking meat.temp using controller.temp

    def isCooked(self, Controller):
        is_Cooking = self. < self.cookTime
        is_Overcooked = self.timePassed > self.cookTime #will have to add some sort of tolerance
        if not(is_Cooking or is_Overcooked):
            controller.notify()               #Now that I have this answer, should it be in controller?

    #I'm going to put this here because it goes with my above comment
    def notify(self, meat):
        #send notification or something?