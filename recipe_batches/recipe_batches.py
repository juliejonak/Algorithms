#!/usr/bin/python

import math

# will receive two dictionaries
# first dict is the recipe to create a batch
# second dict is available ingredients
# return max number of whole batches that can be made from ingredients using that recipe

def recipe_batches(recipe, ingredients):
  # edge case: if ingredients is empty, return 0
  if len(ingredients) == 0:
    return 0

  # store a batch count
  batch_count = 0

  while len(ingredients) != 0:
    for item, amount in recipe.items():
      # if recipe[i] in ingredients:
      if item in ingredients:
        # if subtracted amount below 0:
        if ingredients[item] - recipe[item] < 0:
            return batch_count
        else: 
          # update ingredients amount to subtracted total
          ingredients[item] = ingredients[item] - recipe[item]
      
      # else if recipe[i] not in ingredients:
      else:
        return 0

    batch_count += 1
  
  return batch_count

# Alg runs through N (n based on recipe) * number of batches
# O(n) run time


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 432, 'butter': 153, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))