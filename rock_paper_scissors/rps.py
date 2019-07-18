#!/usr/bin/python

import sys

# input is number of rounds to be played
# returns list of lists of every possible combination of plays that can be made in n rounds, where length = n
def rock_paper_scissors(n):
    # initialize a hashtable = dict()

    # memoiezer function to call recursively and fill hashtable:
        # define all possible moves: ["rock", "paper", "scissors"]
        # handle edge case of 0 rounds
        # base case: if n = 0:
            # return []
        
        # if n rounds already stored, return result
        # if n in cache:
            # return cache[n]
        # otherwise, add it to the cache
        # else:
            # new_list = []
            # for each possible move, iterate through previous n results
            # for i in range(0, moves):
                # sublist = []
                # add to the end of each previous n result the possible move
                # for j in cache[n-1]:
                    # sublist.append(j.append(moves[i]))
                # new_list.append(sublist)
            # cache[n] = new_list
            # return cache[n]
    
    # return memoiezer(n, hashtable)

  pass 

"""
rock
paper
scissors

rock, rock
rock, paper
rock, scissors
paper, rock
paper, paper
paper, scissors
scissors, rock
scissors, paper
scissors, scissors

rock, rock, rock
rock, rock, paper
rock, rock, scissors
rock, paper, rock
rock, paper, paper
rock, paper, scissors
rock, scissors, rock
etc...

each previous list plus rock
each previous list plus paper
each previous list plus scissors
"""
if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')