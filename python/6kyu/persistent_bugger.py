# Kata: Persistent Bugger
# Difficulty: 6 kyu
# URL: https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec/
# 
# Description: 
# Write a function to return the multiplicative persistence of a passed integer. 
#
# Approach:
# Use a while loop to count the number of multiplications of the digits that are required until reaching a single digit number.

def persistence(n):
    i = 0
    while n > 9: 
        m = 1
        for x in list(str(n)):
            m = m * int(x)
        i += 1
        n = m
        
    return i