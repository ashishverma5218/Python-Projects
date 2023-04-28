import random
while True:
    level = input("Easy or Hard ? ").lower()
    if level == "easy":
        no_of_lifes = 1
        answer = random.randint(1, 30)
        while no_of_lifes <= 8:
            user_answer = int(input("Guess a number b/w 1 to 30 ? "))
            if user_answer > 30 or user_answer < 1:
                print("Invalid.... Please Choose b/w 1 to 30 ")
            elif user_answer < answer:
                print("Too low ")
            elif user_answer > answer:
                print("Too high ")
            else:
                print("You win the game...! ")
                print("You take", no_of_lifes, "Chance to finish ")
                break
            print("Chances left ", 8 - no_of_lifes)
            no_of_lifes = no_of_lifes + 1
        if no_of_lifes > 8:
            print("Game Over You loose...!", f"The correct answer is {answer}")
    elif level == "hard":
        no_of_lifes = 1
        answer = random.randint(1, 30)
        while no_of_lifes <= 5:
            user_answer = int(input("Guess a Number b/w 1 to 30 ? "))
            if user_answer > 30 or user_answer < 1:
                print("Invalid.... Please Choose b/w 1 to 30 ")
            if user_answer < answer:
                print("Too low ")
            elif user_answer > answer:
                print("Too high ")
            else:
                print("You win the game...! ")
                print("You take", no_of_lifes, "Chance to finish ")
                break
            print("Chances left ", 5 - no_of_lifes)
            no_of_lifes = no_of_lifes + 1
        if no_of_lifes > 5:
            print("Game Over You loose...! ", f"The correct answer is {answer}")
    play_again = input("Play again Y/N ?").lower()
    if play_again !='y':
        break
