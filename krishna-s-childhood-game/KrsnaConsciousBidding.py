bids = {}
bidding_finished = False

def find_highest_bidding_devotee(bidding_record):
  highest_bid = 0
  winner = ""
  for devotee in bidding_record:
    bid_amount = bidding_record[devotee]
    if bid_amount > highest_bid: 
      highest_bid = bid_amount
      winner = devotee
  print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bidding_finished:
  name = input("Hare Krishna! What is your name, dear devotee?: ")
  price = int(input("Hare Krishna! What is your bid, dear devotee?: $"))
  bids[name] = price
  should_continue = input("Hare Krishna! Are there any other devotees who wish to bid? Type 'yes' or 'no'.\n")
  if should_continue.lower() == "no":
    bidding_finished = True
    find_highest_bidding_devotee(bids)
