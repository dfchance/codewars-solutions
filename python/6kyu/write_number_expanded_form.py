# Kata: Write Number in Expanded Form
# Difficulty: 6 kyu
# URL: https://www.codewars.com/kata/5266876b8f4bf2da9b000362
# 
# Description: 
# Given a number passed as a parameter, return the number as a string in expanded formm.  
#
# Approach:
# Iterate through each digit and create a string by place value, including the correct number of zeroes.   

def expanded_form(num):
    s_num = str(num)
    expanded = s_num[0] + (len(s_num) - 1) * '0'
    n = 1
    
    while n < len(s_num):
        if s_num[n] == '0':
            pass
        else: 
            expanded += ' + '
            expanded += s_num[n] + (len(s_num) - n - 1) * '0'
        n += 1
    
    return expanded