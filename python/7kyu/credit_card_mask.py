# Kata: Credit Card Mask
# Difficulty: 7 kyu
# URL: https://www.codewars.com/kata/5412509bd436bd33920011bc
# 
# Description: 
# Mask all but the last four digits of a passed string.
#
# Approach:
# Return a string with all but the last 4 digits replaced by '#'. 

def maskify(cc):
    l = len(cc)
    if l <= 4:
        return cc
    else:
        cc = "#" * (l - 4) + cc[(l-4):]
        return cc