import random as rand
moves = [0,1,2]
player = int(input("enter 0 for rock, 1 for paper, 2 for scissor"))


rand = rand.randint(0,2)
if (player == 0 and moves[rand] == 0) :
    print("it's both rock, nothing happens.")
elif (player == 0 and moves[rand] == 1) :
     print("you chose rock, computer chose paper, computer wins")
elif (player == 0 and moves[rand] == 2) :
    print("you chose rock, computer chose scissor, you win")

elif (player == 1 and moves[rand] == 0) :
    print("you chose paper, computer chose rock, you win")
elif (player == 1 and moves[rand] == 1) :
    print("it's both paper, nothing happens.")
elif (player == 1 and moves[rand] == 2) :
    print("you chose paper, computer chose scissor, computer wins")

elif (player == 2 and moves[rand] == 0) :
    print("you chose scissor, computer chose rock, computer wins")
elif (player == 2 and moves[rand] == 1) :
    print("you chose scissor, computer chose paper, you win")
elif (player == 2 and moves[rand] == 2) :
    print("it's both scissor, nothing happens.")
else: print("wrong choice")