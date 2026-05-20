# Kata: Pete, the Baker
# Difficulty: 5 kyu
# URL: https://www.codewars.com/kata/525c65e51bf619685c000059/
# 
# Description: 
# Create a function, cakes(), that takes two dictionaries as a parameter and return how many cakes the recipe can make with the available ingredients.    
#
# Approach:
# Determine if there are enough ingredients and then create a list of how many cakes can be made with each ingredient.  Return the minimum.  

def cakes(recipe, available):
    num = []
    for ingredient, amount in recipe.items():
        if ingredient not in available or available[ingredient] < amount:
            return 0
        else:
            num.append(available[ingredient] // amount)
            
    return min(num)