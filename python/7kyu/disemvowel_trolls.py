# Kata: Disemvowel Trolls
# Difficulty: 7 kyu
# URL: https://www.codewars.com/kata/52fba66badcd10859f00097e
# 
# Description: 
# Remove all vowels from the given string and return the result. 

# Original Solution from 
# Approach:
# Iterate through the string, checking each character.  If it is a vowel, remove it. 
def disemvowel(string_):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    n = 0
    while n < len(string_): 
        ch = string_[n]
        # Remove the vowel from the string
        if ch in vowels:
            string_ = string_[0:n] + string_[n+1:]
        # Move to the next letter in the string
        else:
            n += 1
                
    return string_

# Refactored Solution from May 19, 2026
# Approach: 
# Iterate through each letter in the string and create a new string with only consonants. 
def disemvowel(string_):
    vowels = "aeiouAEIOU"
    no_vowels = ""
    for l in string_: 
        if l not in vowels:
            no_vowels += l

    return no_vowels