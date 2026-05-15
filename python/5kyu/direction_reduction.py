# Kata: Directions Reduction
# Difficulty: 5 kyu
# URL: https://www.codewars.com/kata/550f22f4d758534c1100025a
# 
# Description: 
# Write a function that takes an array of complex directions and simplify them to remove needless effort.  
#
# Approach:
# Declare dictionary of opposites and delete consecutive opposites (NORTH / SOUTH) or (EAST / WEST).  

def dir_reduc(arr):
    opposites = {"NORTH": "SOUTH", "SOUTH": "NORTH", "EAST": "WEST", "WEST": "EAST"}
    n = 0
    while n < (len(arr) - 1):
        if opposites[arr[n]] == arr[n + 1]:
            del arr[n + 1]
            del arr[n]
            # Return to start of the array (accounting for next increment)
            n = -1
        n += 1
    return arr