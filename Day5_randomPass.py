import random as rand
num = int(input("how many numbers do you want?\n"))
letter = int(input("how many letters do you want?\n"))
symbol = int(input("how many symbol do you want?\n"))

password_list = []


num_list = ["0","1","2","3","4","5","6","7","8","9"]
letter_list = [ "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z" ]
symbol_list = ["!","@","#","$","%","^","&","*","(",")","-"]

for i in range(num):
    password_list.append(rand.choice(num_list))
    
for i in range(letter):
    password_list.append(rand.choice(letter_list))

for i in range(symbol):
    password_list.append(rand.choice(symbol_list))

rand.shuffle(password_list)

password = ''.join(map(str, password_list))

print("your password is " + password)
