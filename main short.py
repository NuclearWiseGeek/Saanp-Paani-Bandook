import random

'''
1 for Saanp
-1 for Paani
0 for Bandook
'''

computer = random.choice([-1,0,1])
x = input("Enter the choice: ")
dictionary = {"s": 1, "p" : -1 , "b" : 0}
reversedictionary = {1 : "Saanp", -1 :"Paani", 0:"Bandook"}

you = dictionary[x]

# By now we have 2 variables you and computer

print(f"You choose {reversedictionary[you]} \nComputer choose {reversedictionary[computer]} ")

if (computer ==you):
    print("Its a draw!!!")
else:
    if ((computer - you) == -1 or (computer - you) == 2):
        print("you Lose!!")
    else:
        print("You Win!!")

'''
if (computer ==you):
    print("Its a draw!!!")

else:
    if (computer == -1 and you == 0):  (Computer - You) = -1
        print("You Win!!")

    elif (computer == -1 and you == 1): (Computer - You) = -2
        print("You Lose!!")

    elif (computer == 1 and you == 0): (Computer - You) = 1
        print("You Lose!!")

    elif (computer == 1 and you == -1): (Computer - You) =2
        print("You Win!!")

    elif (computer == 0 and you == 1): (Computer - You) =-1
        print("You Win!!")

    elif (computer == 0 and you == -1): (Computer - You) = 1
        print("You Lose!!")
'''
