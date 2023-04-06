from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.
print(logo)
print("Welcome to the secret auction program")

bidders = []

def winner(bidders):
  winning_bid = 0
  winning_person = ''
  for bidder in bidders:
    if bidder["bid"] > winning_bid:
      winning_bid = bidder["bid"]
      winning_person = bidder["name"]
  print(f"The winner is {winning_person} with a bid of ${winning_bid}.")

def bidding():
  continue_bidding = True
  while continue_bidding:
    name = input("What is yout name? ")
    bid = int(input("What's your bid?: $"))
    bidders.append(
      {
        "name": name,
        "bid": bid
      }
    )
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    clear()
    if other_bidders == 'no':
      winner(bidders)
      continue_bidding = False

bidding()