import keyboard
import time
import random
from os import system, name 

loopIncrement = 0
inputVar = int(input("Enter amount of times to swipe: "))
left = 'left'
right = 'right'
LIncrement = 0
RIncrement = 0


for i in range(inputVar):
    LeftOrRight = random.choice([left, right])
    randTime = random.uniform(0.00,4.00)
    keyboard.press_and_release(LeftOrRight)
    print("Swiped: " + LeftOrRight)
    if (LeftOrRight == 'left'):
    	LIncrement +=1
    else:
    	RIncrement +=1
    system('cls')
    time.sleep(randTime)
    print(randTime)
    loopIncrement +=1
    system('cls')
    print("Swiped a total of: " + str(loopIncrement) + " times!")
    print("Swiped Left a total of: " + str(LIncrement) + " times!")
    print("Swiped Right a total of: " + str(RIncrement) + " times!")
    time.sleep(randTime)
    print(randTime)
    system('cls')
    time.sleep(randTime)
    print(randTime)