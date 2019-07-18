#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
def eating_cookies(n, cache=None):
    # Store possible ways to eat the cookie as options to iterate through for solutions [0, 1, 2, 3]
  
    # if there are no cookies, return 1 (only one way to eat 0 cookies)
    # if there are negative cookies, return 0 (not possible to eat negative cookies)

    # iterate through possible ways list:
        # check all possible solutions with i
        # subtract i from n
        # consecutive loops find all possible solutions from new n?
    
    # iterate through possible ways list:
        # check all possible solutions excluding i

    # count total possible iterations from both loops
    # will this include duplicates?

    pass





# Could use a solution that stores memoization. In hash table, store an array at each key, and iterate through the array, adding each possible combo to the final array

# Store these combos at each key so over time, it's quick to add every additional possible combination.

# 1: 1 = 1
# 2: 1 + 1, 2 = 2
# 3: 1 + 2, 2 + 1, 1 + 1 + 1, 3 = 4
# 4: 1 + 3, 3 + 1, 1 + 2 + 1, 1 + 1 + 2, 2 + 2, 1 + 1 + 1 + 1, 4 = 7

if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_cookies = int(sys.argv[1])
        print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
    else:
        print('Usage: eating_cookies.py [num_cookies]')