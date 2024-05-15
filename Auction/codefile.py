def find_winner(bid_info):
    highest_bid = 0
    winner = ""
    for key in bid_info:
        bid_amount = bid_info[key]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = key
    print(f"the winner is {winner} with bid amount of {highest_bid}")
    
bidder_info = {}
other_bidder = True
while other_bidder:
    name = input("Enter name:")
    bid = int(input("What is your bid? "))
    bidder_info[name] = bid 
    other_user = input("Is there another user wanting to bid? ").lower()
    if other_user == "no":
        other_bidder = False
        find_winner(bidder_info)
   

#print(bidder_info)        
