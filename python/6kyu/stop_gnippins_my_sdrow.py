# Kata: Stop gnippinS my sdroW!
# Difficulty: 6 kyu
# URL: https://www.codewars.com/kata/5264d2b162488dc400000001
# 
# Description: 
# Write a function that takes a string and returns the same stringn with any words greater or equal to 5 characters reversed.  
#
# Approach:
# Iterate through the string and reverse words that are greater than or equal to 5 characters.  Return the new joined string.  

def spin_words(sentence):
    words = []
    for word in sentence.split(" "):
        if len(word) >= 5:
            word = word[::-1]
        words.append(word)
    return " ".join(words)