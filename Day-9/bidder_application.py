import os
from art import logo
print(logo)

final_bids = {}

#find the hightst bidder

def find_max_bidder(bidding_record):
    highest_bid = 0 
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner}, with {highest_bid} $")
        

more_bidder = False
while not more_bidder:
    name = input("What is your name? ")
    price = int(input("What is your bid amount? $"))
    final_bids[name] = price
    aviablity = input("Are there any one to bid? ('yes' or 'no')")
    if aviablity == "no":
        more_bidder = True
        find_max_bidder(final_bids)
    elif aviablity == "yes":
        os.system('cls')

