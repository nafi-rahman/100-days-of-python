print("welcome to the island, your mission is to find the treasure\n There is two roads infront of you, one going left and the other going right.\n where would you like to go? \n")

while True:
    choice = input()
    if choice.lower() == "right":
        print ("you were ambushed by wild animals and died.")
        break
    elif choice.lower() == "left":
        print("it is a long stretch of road with trees on both sides of the road and you're walking down it.\n")
        break
    else: print("invalid choice try again.")

print("the tide is high now and the road infront is submerged in water. do you wait or do you swim? \n")


 
while True:
    choice = input()
    if choice.lower() == "swim":
        print ("The water is infested with crocs and you were killed by one.")
        break
    elif choice.lower() == "wait":
        print("The water came down and the road infront is clear now. \n")
        break
    else: print("invalid choice try again.")

print("there are three doors at the end of the road you were walking, the doors are of different color. from left to right, it's red, yellow, blue. which door would you choose? \n")

while True:
    choice = input()
    if choice.lower() == "red" or choice.lower() == "blue"  :
        print ("you fell into a pit full of snakes and died.")
        break
    elif choice.lower() == "yellow":
        print("behold, the treasure is infront of you. you have won. \n")
        break
    else: print("invalid choice try again.")