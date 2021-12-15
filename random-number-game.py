import random
import math

print("**********************")
print("*                    *")
print("* RANDOM NUMBER GAME *")
print("*                    *")
print("**********************")

# get lower bound from user
lower = int(input("Enter lower bound: "))

# get upper bound from user, ensure it is greater than lower bound
upper = lower
while upper <= lower:
    upper = int(input("Enter upper bound: "))

# generate a random number between the upper and lower bounds
print("Generating random number between %d and %d ..." %(lower, upper))
numToGuess = random.randint(lower, upper)

maxGuesses = round(math.log(upper - lower + 1, 2))
print("You have %d chances to guess!" %(maxGuesses))

numOfGuesses = 0

# keep asking user to guess until they guess correctly
while numOfGuesses < maxGuesses:
    numOfGuesses += 1

    # get the guess from user
    guess = int(input("Enter your guess: "))

    # if they guess correctly, we need to break from the loop
    if numToGuess == guess:
        print("Congrats! You're right!")
        break
    # else if they guess wrong, we continue...
    # if guess too low, hint
    elif numToGuess > guess:
        print("You guessed too low!")
    # if guess too high, hint
    elif numToGuess < guess:
        print("You guessed too high!")

if numOfGuesses >= maxGuesses:
    print("Better luck next time! The number was %d" %(numToGuess))