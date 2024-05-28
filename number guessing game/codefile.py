import random

num_list = list(range(1,101))
computer_num = random.choice(num_list)

def take_guess():
    user_guess = int(input("Make a guess:"))
    if user_guess == computer_num:
        return True
    elif user_guess < computer_num:
        print("Too low.")
        return False
    elif user_guess > computer_num:
        print("Too high.")
        return False
    
def guess_game(a):
    win = False
    while win == False:
        for i in range(a, 0, -1):
            print(f"You have {i} attempts remaining")
            result = take_guess()
            if result == True:
                print("You win!")
                win = True
        if result == False:
            print("Out of guesses. You loose.")
            break;
    
    
print("Welcome to the number guessing game\nI am thinking of a number between 1 to 100.")
level = input("Choose the difficulty level- 'easy' or 'hard':").lower()
if level == 'easy':
    attempts = 10
    guess_game(attempts)
else:
    attempts = 5
    guess_game(attempts)
    
