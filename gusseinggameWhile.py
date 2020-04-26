import random

highest = 10
guess = random.randint(1, highest)
print(guess)

while True:
    answer = 0
    answer = int(input("Please choose the number: {}".format(highest)))
    if answer == guess:
        print("You guessed it right")
        break
    elif answer == 0:
        print("You are done asshole, I will quit you out")
        break
    elif answer > guess:
        print("Please guess lower number")
        continue
    else:
        print("Please guess Higher number")
        continue




