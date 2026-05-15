# Kata: Create Phone Number
# Difficulty: 6 kyu
# URL: https://www.codewars.com/kata/525f50e3b73515a6db000b83
# 
# Description: 
# Take an array of digits and return them properly formatted as a phone number, following the correct order of the array.   
#
# Approach:
# Iterate through the array, concatenating numbers recast as strings with the formatting symbols in the correct positions. 

def create_phone_number(n):
    str_num = "("
    count = 0
    for num in n: 
        str_num += str(num)
        if count == 2:
            str_num += ") "
        if count == 5: 
            str_num += "-"
        count += 1
    
    return str_num