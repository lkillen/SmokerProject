from Grill import Grill
from Charcoal import Charcoal
from Meat import Meat
from Controller import Controller
from Fan import Fan
import parser

myCharcoal = Charcoal(0, 140, 100, 500, 0)

print('How long do you want to cook the meat for?')
cookTime = input()
myMeat = Meat('beef', 0 , False, 0, cookTime)
myFan = Fan(False, False, myCharcoal)
myGrill = Grill(myCharcoal, myMeat)
myController = Controller(myFan, 0, 250, myCharcoal)


cont = 'start'
while cont != 'end':
   a = eval(parser.expr(input()).compile())
   b = eval(parser.expr(input()).compile())
   if a > b:
       print("A")
   elif b > a:
       print("B")
   else:
       print("C")
   cont = input()

   #fn takes a string (ex "27 - 3(14 + 6)")
   #myGrill.execute()
    #myController.execute()
    #print(myGrill.charcoal.temp)
    #print(myGrill.temp)
    #print('looped')
    #cont = input()




#Push to GitHub module(?)
#Create fan
#Mess around in the loop - put myGrill in the loop