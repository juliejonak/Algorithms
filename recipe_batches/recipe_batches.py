#!/usr/bin/python

import math

# will receive two dictionaries
# first dict is the recipe to create a batch
# second dict is available ingredients
# return max number of whole batches that can be made from ingredients using that recipe

def recipe_batches(recipe, ingredients):
  # edge case: if ingredients is empty, return 0
  # store a batch count

  # while items in ingredients:
    # for loop iterates over ingredients:
      # if recipe[i] not in ingredients:
        # return 0
      # elif recipe[i] in ingredients:
        # subtract recipe[i] amount from ingredients
        # if subtracted amount below 0:
          # return batch_count
        # else: 
          # update ingredients amount to subtracted total
  pass 


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))