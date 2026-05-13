
# Kata: Disemvowel Trolls
# Difficulty: 7 kyu
#
# Description: 
# Remove all vowels from the given string and return the result. 
#
# Approach:
# Iterate through the string, checking each character.  If it is a vowel, remove it. 


def disemvowel(string_):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    no_vowels = ""
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

