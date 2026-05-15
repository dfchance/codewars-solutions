# Kata: Find the Parity Outlier
# Difficulty: 6 kyu
# URL: https://www.codewars.com/kata/5526fc09a1bbd946250002dc
# 
# Description: 
# Given an array of numbers, find the outlier (the odd in a sea of evens, or the even in a sea of odds). 
#
# Approach:
# Iterate through the array of numbers to determine if it is majority odd or even.  Then, find the outlier using the modulo operator. 

def find_outlier(integers):
    e_count = 0
    o_count = 0
    for n in integers:
        if n % 2 == 0:
            e_count += 1
            print("N: " + str(n) + " E: " + str(e_count))
        else:
            o_count += 1
            print("N: " + str(n) + " O: " + str(o_count))

    if e_count == 1:
        for n in integers:
            if n % 2 == 0:
                return n
    else:
        for n in integers:
            if n % 2 != 0:
                return n
            
def main():
    find_outlier([3, 4, 5, 7, 9])

if __name__ == "__main__":
    main()