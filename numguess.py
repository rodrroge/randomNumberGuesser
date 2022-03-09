import random

#generates random num 1 - 10
random_number = random.randint(1, 10)
#used to check random number
#print(random_number)

life = 2

#asks user for guess
guess = input("Guess a number 1 - 10? ")

while life != 0:
    if int(guess) == random_number:
        print("you win")
        exit()
    else:
        guess = input("Try again, what is your guess? ")
        life -= 1

print("You lose >:)")
