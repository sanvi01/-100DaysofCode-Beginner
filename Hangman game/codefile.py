#Step 4

import random

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

end_of_game = False
words = ["apple","green","hammer","hands","beekeeper"]
answer = random.choice(words)
lives = 6
output = []
for l in answer:
    output += "_"

print("Welcome to the game of hangman!")
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if guess in answer:
        for i in range(len(answer)):
            letter = answer[i]
            if letter == guess:
                output[i] = letter
    else:
        lives -= 1
        if lives == 0:
            end_of_game = True
        else:
            print(f"{guess} not in word")
        print("You loose")

    print(f"{' '.join(output)}")

    if "_" not in output:
        end_of_game = True
        print("You win.")
    
    print(stages[lives])
