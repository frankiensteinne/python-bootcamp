from os import system
from art import logo

# Create empty list to store bidder's data
bids = {}
# Create a boolean for state
is_finish = False

def find_winner(bids):
    highest_bid = 0
    winner = ""

    for bidder in bids:
        bid_amount = bids[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of PhP {highest_bid}")

# State Loop
while not is_finish:
    print(logo)
    name = input("What is your name?: ").capitalize()
    price = int(input("What is your bid?: "))
    bids[name] = price
    next_bidder = input("Is there another bidder after you? Yes or No: ").lower()
    
    if next_bidder == "no":
        system("clear")
        print(logo)
        is_finish = True
        find_winner(bids)
    elif next_bidder == "yes":
        system("clear")