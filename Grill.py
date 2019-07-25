class Grill:

    charcoal = 'charcoal'       # class variable shared by all instances
    meat = 'meat'
    controller = 'controller'
    temp = 'temp'

    def __init__(self, a1, a2, a3):           #This is called an initializer
        self.charcoal = a1          # instance variable unique to each instance
        self.meat = a2
        self.controller = a3
        self.temp = 0

