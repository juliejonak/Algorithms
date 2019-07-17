#!/usr/bin/python

import argparse

# receives list of prices
# returns the maximum profit made from a single buy and sell
# find profit by subtracting the buy price from the sell price

def find_max_profit(prices):
    # Edge case: prices does not contain enough elements
    if len(prices) < 2:
        return "Error: Price list must contain at least two prices."

    # store a max_profit
    max_profit = float("-inf")

    # optional: store prices that lead to max profit in case information is useful 
    buy_price = 0
    sell_price = 0

    # iterate through the list
    for i in range(0, len(prices)-1):
        try:
            # set curr_min to first item in prices, iterate through until second to last item
            curr_min = prices[i]

            # inner loop, iterate through following list items
            for j in range(i+1, len(prices)):
                # test if prices[j] - curr_min is > max_profit
                if prices[j] - curr_min > max_profit:
                    # if greater than, update max profit
                    max_profit = prices[j] - curr_min
                    buy_price = curr_min
                    sell_price = prices[j]

                    print(f"To maximize profit, you should buy at {buy_price} and sell at {sell_price} for ${max_profit} in profit.")
        except:
            return "Invalid data in list. Integers only."

    return max_profit

# Nested loop, O(n^2) time efficiency


# if __name__ == '__main__':
#   # This is just some code to accept inputs from the command line
#   parser = argparse.ArgumentParser(description='Find max profit from prices.')
#   parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
#   args = parser.parse_args()

#   print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))
