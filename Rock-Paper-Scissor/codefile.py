import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

game_image = [rock, paper, scissors]

user_choice = int(input("Choose 0 for rock, 1 for paper, 2 for scissors - "))
if user_choice >= 3 or user_choice < 0:
    print("Invalid input, you lose.")
else:
    print(game_image[user_choice])
    
    comp_choice = random.randint(0,2)
    print(f"Computer chose {comp_choice}")
    print(game_image[comp_choice])
        
    if user_choice == 0 and comp_choice == 2:
        print("You lose")
    elif user_choice == 2 and comp_choice == 0:
        print("You lose")
    elif user_choice < comp_choice:
        print("You lose")
    elif user_choice > comp_choice:
        print("You win!")
    elif user_choice == comp_choice:
        print("Its a draw.")
