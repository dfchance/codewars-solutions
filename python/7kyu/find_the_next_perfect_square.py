# Kata: Find the Next Perfect Square!
# Difficulty: 7 kyu
# URL: # URL: https://www.codewars.com/kata/56269eb78ad2e4ced1000013
# 
# Description: 
# Take an integer parameter and return the next perfect square if it is a perfect square.  Otherwise, return -1.
#
# Approach:
# Check if a number sq is a perfect square and calculate the next perfect square or return -1 if it is not a perfect square. 

def find_next_square(sq):
    return -1 if sq ** 0.5 != int(sq ** 0.5) else ((sq ** 0.5) + 1) ** 2
