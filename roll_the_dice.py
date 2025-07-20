import random
while True:
    input("press enter to roll a dice :)")
    dice=random.randint(1,6)
    print("woooohoooo you rolled dice and output is : ",dice)
    again=input("roll your dice again 1/0: ")
    if again==1 :
        print("thanks <3")
    elif again==0 :
        print("it was nice playing with you. come again")
        break
    else:
        print("your input is not valid ")
