stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
word_list =['dilwale','pathan','dhamaal','welcome']
import random
chosen_word = random.choice(word_list)

end_of_game = False
#TODO-1: - Create a variable called 'lives' to keep track of the number of lives left.
lives = 6
#Create blanks
display = []
for _ in range(len(chosen_word)):
    display+="_"
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    # Check guessed letter
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    # TODO-2: - If guess is not a letter in the chosen_word,
    # Then reduce 'lives' by 1.
    # If lives goes down to 0 then the game should stop and it should print "You lose."
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")
    # Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")
    #print the stages
    print(stages[lives])
