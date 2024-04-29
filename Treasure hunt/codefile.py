print("Welcome to Treasure island.\nYour mission is to find the hidden Treasure.")

choice1 = input("You are at a crossroad,where would you like to go?Type 'left' or 'right'.\n").lower()
if choice1 == "left":
    choice2 = input("You reached a lake with an island in the middle.Type 'wait' to wait for a boat.Type 'swim' to swim across.\n").lower()
    if choice2 == "wait":
        choice3 = input("Arrived the island unharmed.There are three houses- red, blue and yellow.Which color do you choose?"\n).lower()
        if choice3 == "red":
            print("House on fire.Game Over.")
        elif choice3 == "blue":
            print("Haunted house.Game Over.")
        elif choice3 == "yellow":
            print("You win!")
    else:
        print("You got attacked by an aligator.Game Over.")
else:
    print("You fell into a hole.Game Over.")
    
