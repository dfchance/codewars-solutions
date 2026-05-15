# Kata: Duplicate Encoder
# Difficulty: 6 kyu
# URL: https://www.codewars.com/kata/54b42f9314d9229fd6000d9c
# 
# Description: 
# Take a string as parameter and replace duplicate letters with ) and singly-occurring letters with (. Return a string of ( and ). Ignore case. 
#
# Approach:
# Check each letter in the word to see if it appears more than once.  If so, add ) to a new string, otherwise add (. 

def duplicate_encode(word):
    n = 0
    word = word.lower()
    encoded = ""
    while n < len(word):
        l = word[n]
        if n == 0:
            if l in word[(n + 1):]:
                encoded += ")"
            else:
                encoded += "("
        elif n == (len(word) - 1):
            if l in word[:(n - 1)]:
                encoded += ")"
            else: 
                encoded += "("
        else: 
            if l in word[(n + 1):] or l in word[:n]:
                encoded += ")"
            else: 
                encoded += "("
        n += 1
            
    return encoded
