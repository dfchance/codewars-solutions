# Kata: Descending Order
# Difficulty: 7 kyu
# URL: https://www.codewars.com/kata/5412509bd436bd33920011bc
# 
# Description: 
# Return a non-negative integer number with its digits in descending order. 
# 
# Approach:
# Use list functions to sort and reverse and then concatenate and cast as an integer.  

def descending_order(num):
    l = [int(d) for d in str(num)]
    l.sort()
    l.reverse()
    s = ""
    for n in l:
        s += str(n)
    return int(s)