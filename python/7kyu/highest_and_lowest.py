# Kata: Highest and Lowest
# Difficulty: 7 kyu
# URL: # URL: https://www.codewars.com/kata/554b4ac871d6813a03000035/
# 
# Description: 
# Given a string of space-separated numbers, return the highest and lowest value as a string with the numbers separated by a space.
#
# Approach:
# Return the max using int() in the split string plus a string plus the min using the same procedure. 

def high_and_low(numbers):
    return str(max(int(x) for x in numbers.split(' '))) + " " + str(min(int(x) for x in numbers.split(' ')))
