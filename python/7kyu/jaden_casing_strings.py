# Kata: Jaden Casing Strings
# Difficulty: 7 kyu
# URL: https://www.codewars.com/kata/5390bac347d09b7da40006f6
# 
# Description: 
# Take a string as a parameter and return it with the first letter of each word capitalized. 
# 
# Approach:
# Use list comprehension and the join function to return a string with each word capitalized.  

def to_jaden_case(string):
    return " ".join(word.capitalize() for word in string.split(" "))