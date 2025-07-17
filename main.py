import random
'''
1 for snake
-1 for water
0 for gun
'''
yourDict = {"s":1,"w":-1,"g":0}
reverseDict = {1:"snake",-1:"water",0:"gun"}
for i in range(5):
    computer = random.choice([1,-1,0])
    youstr = input("enter your choice  ")
    you = yourDict[youstr]
    print(f"you chose {reverseDict[you]}\n computer chose {reverseDict[computer]}")
    if(computer==you):
        print("draw")
    else:
        if(computer==1 and you == -1):
            print("you lose!")
        elif(computer==-1 and you==1):
            print("you win!")
        elif(computer==0 and you == -1):
            print("you lose!")
        elif(computer==1 and you==0):
            print("you win!")
        elif(computer==1 and you == -1):
            print("you lose!")
        elif(computer==-1 and you==0):
            print("you win!")
        else:
            print("something is wrong")