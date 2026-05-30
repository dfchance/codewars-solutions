# Kata: String Ends With? 
# Difficulty: 7 kyu
# URL: https://www.codewars.com/kata/54c27a33fb7da0db0100040e/
#
# Description: 
# Determine if the integer passed is a perfect square.
#
# Approach:
# Return true if the integer is greater or equal to 0 and has a whole number square root. 

def is_square(n):    
    return True if n >= 0 and n ** 0.5 == int(n**0.5) else False