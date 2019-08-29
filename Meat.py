class Meat:

    protein = 'protein'               #What these do is set an initial value
    temp = 'temp'
    cooked = 'cooked'
    time = 'time'
    cookTime = 'cookTime'

    def __init__(self, protein, temp, cooked, time, cookTime):
        self.protein = protein
        self.temp = temp
        self.cooked = temp
        self.time = time
        self.cookTime = cookTime

    def how_long(self):
        print('How long would you like to smoke your food?')
        self.cookTime = input()


    def cook_temp(self):
        #This is the temperature we would like to controller.temp probe to stay at
        print('What temperature would you like to smoke the meat at?')
        self.temp = input()


    def time_passed(self):#This would start a timer once the controller.temp reaches the cookTemp
        return 0

    def desired_temp(self, controller):
        return 0

    def is_cooked(self, controller):
        is_cooking = self.time < self.cookTime
        is_overcooked = self.time > self.cookTime #will have to add some sort of tolerance
        if not is_cooking or is_overcooked:
            controller.notify()               #Now that I have this answer, should it be in controller?


    def notify(self, meat):#send notification or something?
        return 0