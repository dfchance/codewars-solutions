# Kata: Roman Numerals Decoder
# Difficulty: 6 kyu
# URL: https://www.codewars.com/kata/51b6249c4612257ac0000005/
# 
# Description: 
# Write a function that takes a roman numeral string as input and returns its value in standard decimal form.  
#
# Approach:
# Iterate through the string and add each value, subtracting values accordingly when they come ahead of larger values (IX = 9).  
 
def solution(roman : str) -> int:
    values = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    standard, i = 0, 0
    
    # iterate through the roman numeral string, changing each value
    while i < len(roman): 
        l = roman[i]
        # check if at the last value
        if i == len(roman) - 1:
            value = values[l]
            standard += value
            break
        # compare current value with next to determine appropriate conversion
        n = roman[i + 1]
        value = values[l]
        next = values[n]
        if value < next:
            value = -value
        standard += value
        i += 1
        
    return standard
