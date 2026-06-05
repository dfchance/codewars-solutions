# Kata: Array.diff
# Difficulty: 6 kyu
# URL: https://www.codewars.com/kata/523f5d21c841566fde000009
# 
# Description: 
# Given two lists, return the first list with all instances of the second list elements removed.  
#
# Approach:
# Iterate through each element in the second list and remove them from a.  Use recursion to find all instances.
 
def array_diff(a, b):
    for el in b:
        if el in a:
            a.remove(el)
            array_diff(a, b)
    return a