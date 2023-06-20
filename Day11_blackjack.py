logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
import random as rand
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

player = []
computer = []
ptotal = 0
ctotal = 0
Eog = False

def hasBlackJack(usr):
    if len(usr) == 2 and count(usr) ==21:
        return True
    else:
        return False

def add_card(user):
    temp = rand.choice(cards)
    if temp == 11:
        if count(user) < 21:
             user.append(temp)
        else:
            user.append(1)  
    else:
        user.append(temp)
    return

def count(user):
    temp = 0
    for items in user:
        temp += items
    return temp



def player_moves():
    while True:
        choice = input("do you want to draw more cards? 'y' for yes and 'n' for no\n")
        if choice.lower() == "y":
            add_card(player)
            print(f"your cards are {player} and the total value is {count(player)}")
        elif choice.lower() == "n":
            computer_moves()
            break
        else:
            print("wrong  choice")

def computer_moves():
    while True:
        if count(computer) < 17:
            add_card(computer)
        else:
            break

def blackjack():
    for i in range(2):
        add_card(player)
        add_card(computer)
    print(f"your cards are {player} and the total value is {count(player)}")
    print(f"computer's cards are [{rand.choice(computer)}, *]")
    player_moves()
    
    if hasBlackJack(computer):
        print("computer has a blackjack. you lose.")
    elif hasBlackJack(player) == True and hasBlackJack(computer) == False:
        print("you win")
    else:
        if count(player) > count(computer):
            if count(player) > 21:
                if count(computer)  <= 21:
                    print("computer wins, you have more than 21")
                else:
                    print("you win")    
        elif count(computer) > count(player)  :
            if count(computer) > 21:
                if count(player)  <= 21:
                    print("you win, computer has more than 21")
                else:
                    print("computer wins")
        else:
            print("error") 
print(logo)
print("welcome to blackjack")    
blackjack()