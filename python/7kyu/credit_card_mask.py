# Kata: Credit Card Mask
# Difficulty: 7 kyu
# URL: https://www.codewars.com/kata/5412509bd436bd33920011bc
# 
# Description: 
# Mask all but the last four digits of a passed string.
#

# Original Solution from May 12, 2026
# Approach:
# Return a string with all but the last 4 digits replaced by '#'. 
def maskify(cc):
    l = len(cc)
    if l <= 4:
        return cc
    else:
        cc = "#" * (l - 4) + cc[(l-4):]
        return cc
    
# Refactored Solution from May 24, 2026
# Approach:
# Simplify into a single return statement using a concatenated string with all but the last 4 digits replaced by '#'. 
def maskify(cc):
    return cc if len(cc) <= 4 else "#" * (len(cc) - 4) + cc[-4:]