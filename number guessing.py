import random
import time

a=random.randint(1,50)
i=0
x=0
print("NUMBER GUESSING GAME\n")
while(x!=a):
        x=int(input("Guess the number: "))
        if x>a:
            print("\t Gueesed number is larger \n")
        elif x<a:
            print("\t Guessed number is smaller\n")
        i+=1
time.sleep(1/2)
print("You got it!!!")
print("You took",i,"tries")
time.sleep(1)
#gbkmkb
