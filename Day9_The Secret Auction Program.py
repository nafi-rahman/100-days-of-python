import os
print("welcome to the secret auction app")
auction = {}
flag = True
hkey = ""
hnum = 0
while True:
    if flag == True:
        name = input("enter your name\n")
        bid = int(input("enter the amount of your bid\n"))
        auction[name] = bid
        choice = input("type yes to add more bets and no to stop\n")
        if choice.lower() == "yes":
            os.system('CLS')
        else:
            flag = False
    else:
        break

for keys in auction:
    if auction[keys] > hnum:
        hkey = keys
        hnum = auction[keys]
        
print(f"{hkey} bid {hnum}")