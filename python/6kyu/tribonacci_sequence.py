# Kata: Tribonacci Sequence
# Difficulty: 6 kyu
# URL: https://www.codewars.com/kata/556deca17c58da83c00002db
# 
# Description: 
# Take a signature list of 3 digits and return a list of the first n elements in the Tribonacci sequence (each subsequent digit adds the three previous).
#
# Approach:
# Check n to determine number of elements and then append the correct number of sums to the original list. 

def tribonacci(signature, n):
    if n <= 3:
        return signature[0:n]
    
    for x in range(n - 3):
        signature.append(signature[x] + signature[x + 1] + signature[x + 2])
    
    return signature
