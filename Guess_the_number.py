import random

n = random.randint(1, 30)
number_of_guesses = 1
print("Number of guesses is limited to only 5 times ")
while number_of_guesses <= 5:
    guess_number = int(input("Guess the number in between(1-30) :"))
    if guess_number < n:
        print("too low")
    elif guess_number > n:
        print("too high")
    else:
        print("\nyou won the game\n")
        print(number_of_guesses, "no of guesses you took to finish")
        break
    print("no. of guesses left", 5 - number_of_guesses)
    number_of_guesses = number_of_guesses + 1
if number_of_guesses > 5:
    print(" game over \n You loose the game")
