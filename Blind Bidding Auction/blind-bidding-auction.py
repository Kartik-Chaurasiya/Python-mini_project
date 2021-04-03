from replit import clear #clear the console
print('Welcome to the Blind Auction......')
print('''

                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\
                         `'-------'`
                       .-------------.
                      /_______________\ ''')
bidding_done = True
bids = {}

def highest_bidder(bids):
    highest_bid = 0
    highest_bidder = ''
    for bidder in bids:
        if highest_bid < bids[bidder]:
            highest_bid = bids[bidder]
            highest_bidder = bidder
    print(f'The Winner is {highest_bidder} with the bid of {highest_bid}.')
        

while bidding_done:
    name = input("Enter Your Name: ")
    bid = int(input("Enter Your Bid: "))
    bids[name] = bid
    user_choice = input("Are there any more bidders. \n press 'yes' if there are else 'no' to get the results: ")
    if user_choice == 'no':
        bidding_done = False
        highest_bidder(bids)
    elif user_choice == 'yes':
        clear()

