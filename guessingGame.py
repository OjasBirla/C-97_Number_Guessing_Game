import random

number = random.randint(1, 9)
chances = 5
print("Guess the Number between 1 to 9")
inp = int(input("Try Guesssing the Nunber, The Number is Between 1 and 9"))

while True:
    chances -= 1
    if inp == number:
        print("You Got it")

    elif inp < number:
        print("Your Guess is lower than the Number")

    else:
        print("Your Guess is Higher than the Number")
    
    inp = int(input("Try Guesssing the Nunber Again"))

print("Sorry, You Lose")