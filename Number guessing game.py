import random

# generate a random number between 1 and 100
number = random.randint(1, 100)

# keep track of the number of guesses
guesses = 0

while True:
    # ask the user to guess the number
    guess = int(input("Guess a number between 1 and 100: "))

    # increase the number of guesses
    guesses += 1

    # check if the guess is correct
    if guess == number:
        print(f"Congratulations! You guessed the number in {guesses} guesses.")
        break
    elif guess < number:
        print("Too low. Try again.")
    else:
        print("Too high. Try again.")
