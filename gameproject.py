import random

target = random.randint(1,100)
# print(randnum)

while True:
    userchoice = input("enter the choise or quit(Q) :" )
    if(userchoice=="Q"):
        break

    userchoice = int(userchoice)

    if(userchoice==target):
        print("success >>  Corect guess...")
        break

    elif(userchoice < target):
        print("your number is small , Take a big guess")

    else:
        print("your number is large , take a small guess")


print("___Game over___")    