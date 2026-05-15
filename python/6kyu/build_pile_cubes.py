# Kata: Build a Pile of Cubes
# Difficulty: 6 kyu
# URL: https://www.codewars.com/kata/5592e3bd57b64d00f3000047
# 
# Description: 
# Given a parameter, m, determine the number of cubes, n, necessary to build a building of that size using the formula
# n**3 + (n-1)**3 + (n-2)**3 + ... + 1**3.  Return -1 if no such n exists.  
#
# Approach:
# Begin with the top and build layer by layer until volume equals or exceeds the passed parameter.  Return n if the volume equals m. 

def find_nb(m):
    vol = 1
    n = 1
    while vol < m:
        n += 1
        vol = vol + n**3
    
    if vol == m:
        return n
    else:
        return -1
