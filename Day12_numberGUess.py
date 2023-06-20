import random as rand
numbers = [x for x in range(1,101)]

num = rand.choice(numbers)
lives = 5


while True:
    choice = int(input("guess a random number from 1-100:\n"))
    if choice >= num:
        if choice == num:
            print(f"{choice} is the number: {num}, congratulations")
            break
        else:
            print(f"{choice} is greater than the number") 
            lives -=1
            print(f"{lives} lives remaining")
            if lives == 0:
                print(f"the number is {num}")
                break
            
    elif choice <= num:
        if choice == num:
            print(f"{choice} is the number: {num}, congratulations")
            break
        else:
            print(f"{choice} is lower than the number")
            lives -=1
            print(f"{lives} lives remaining") 
            if lives == 0:
                print(f"the number is {num}")
                break 
    else:
        print(f"congratulations! {choice} is the number: {num}.")
        break