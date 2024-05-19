import random

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
user_cards = []
computer_cards = []

def deal_card():
    card = random.choice(cards)
    return card

def BlackJack():
    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    print(f"Your cards: {user_cards}, Current total:{sum(user_cards)}")
    print(f"Computer's first card: {computer_cards[0]}")
    while sum(user_cards)<21:
        add_card = input("Do you want another card? 'y' or 'n': ")
        if add_card == 'y':
            user_cards.append(deal_card())
            print(f"Your cards: {user_cards}, Current total:{sum(user_cards)}")
            print(f"Computer's first card: {computer_cards[0]}")
        elif add_card == 'n':
            break;
    print(f"Your final cards: {user_cards}, Your final total:{sum(user_cards)}")
    if sum(computer_cards)<=17:
        computer_cards.append(deal_card())
        print(f"Computer's final cards: {computer_cards}, Computer's final total:{sum(computer_cards)}")
    else:
        print(f"Computer's final cards: {computer_cards}, Computer's final total:{sum(computer_cards)}")
        
    user_total = sum(user_cards)
    computer_total = sum(computer_cards)
    if user_total == 21 and len(user_cards) == 2:
        print("You win with a blackjack!!")
    elif user_total>computer_total and user_total<=21:
        print("You win!!")
    elif user_total>computer_total and user_total>21:
        print("You lose")
    elif user_total<computer_total and computer_total>21:
        print("You win!!")
    elif user_total<computer_total and computer_total<=21:
        print("You lose")
    elif user_total == computer_total:
        print("Draw")

game_on = input("Do you want to play game of BlackJack?'y' or 'n': ")
if game_on == 'y':
    BlackJack()
else:
    print("ok bye..")
    
      
