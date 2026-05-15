# Kata: Create Phone Number
# Difficulty: 6 kyu
# URL: https://www.codewars.com/kata/525f50e3b73515a6db000b83
# 
# Description: 
# Take an array of digits and return them properly formatted as a phone number, following the correct order of the array.   

# Original Solution from May 11, 2026
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

# Refactored Solution from May 14, 2026
# Approach:
# Use f-string with direct indexing to format phone number in one line. 
def create_phone_number(n):
    return f"({n[0]}{n[1]}{n[2]}) {n[3]}{n[4]}{n[5]}-{n[6]}{n[7]}{n[8]}{n[9]}"
