#!/usr/bin/python

import argparse

def find_max_profit(prices):
  pass

# receives list of prices
# returns the maximum profit made from a single buy and sell
# find profit by subtracting the buy price from the sell price


# set prices[0] at the first curr_min to test against following prices
# store a max_profit
# iterate through the list
# inner loop, iterate through following list items
# test if prices[j] - curr_min is > max_profit
# if greater than, update max profit

# optional: store prices that lead to max profit in case information is useful 

# edge cases? must handle possible negative max_profit. empty price list. non-integer item in list.






print(find_max_profit([10, 7, 5, 8, 11, 9])) #6



# if __name__ == '__main__':
#   # This is just some code to accept inputs from the command line
#   parser = argparse.ArgumentParser(description='Find max profit from prices.')
#   parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
#   args = parser.parse_args()

#   print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))
