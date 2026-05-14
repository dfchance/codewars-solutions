# Kata: Bit Counting
# Difficulty: 6 kyu
#
# Description: 
# Write a function that takes an integer as input and returns the number of '1' bits in its binary representation.  
#
# Approach:
# Conver to binary and iterate through the string, counting the number of '1's.  
 
def count_bits(n):
    b = format(n, 'b')
    m = 0
    for l in b: 
        if l == '1':
            m += 1
    return m