#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
def eating_cookies1(n, cache=None):
    # if there are no cookies, return 1 (only one way to eat 0 cookies)
    if n == 0:
        return 1
    # if there are negative cookies, return 0 (not possible to eat negative cookies)
    if n < 0:
        return 0

    # the count is equal to the sum of the count of n-1, n-2, and n-3 (all possible ways to start eating the cookies)
    count = (eating_cookies(n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache))

    return count

# Could use a solution that stores memoization. In hash table, store an array at each key, and iterate through the array, adding each possible combo to the final array

# Store these combos at each key so over time, it's quick to add every additional possible combination.

def eating_cookies(n, cache=None):
    hashtable = dict()
    
    def memoizer(n, cache):
        if n == 0:
            return 1

        if n < 0:
            return 0

        if n in cache:
            return cache[n]
        else:
            cache[n] = memoizer(n-1, cache) + memoizer(n-2, cache) + memoizer(n-3, cache)
            return cache[n]
    
    return memoizer(n, hashtable)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_cookies = int(sys.argv[1])
        print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
    else:
        print('Usage: eating_cookies.py [num_cookies]')