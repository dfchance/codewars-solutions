# Kata: RGB to Hex Conversion 
# Difficulty: 5 kyu
# URL: https://www.codewars.com/kata/513e08acc600c94f01000001
# 
# Description: 
# Create a function that takes RGB values and returns the hexadecimal result.  Values outside the range 0-255 are rounded to the closest possible value.    
#
# Approach:
# Convert each RGB value individually using division and then concatenate the hex RGB values to return a string. 

def rgb(r, g, b):
    # add hexadecimal values one value at a time
    s = hex_con(r)
    s = s + hex_con(g)
    s = s + hex_con(b)
    
    return s

def hex_con(n):
    # edge cases
    if n > 255: 
        return "FF"
    if n < 0: 
        return "00"
    
    # dictionary of double-digit values
    values = {
        10: "A",
        11: "B",
        12: "C",
        13: "D",
        14: "E",
        15: "F"
    }
    
    # calculate the first remainder
    r = n % 16
    if r in values:
        s = values[r]
    else:
        s = str(r)
    
    # calculate the second remainder
    r = n // 16 % 16
    if r in values:
        s = values[r] + s
    else:
        s = str(r) + s
    
    return s
