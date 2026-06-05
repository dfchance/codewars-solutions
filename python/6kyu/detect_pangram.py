# Kata: Detect Pangram
# Difficulty: 6 kyu
# URL: https://www.codewars.com/kata/545cedaa9943f7fe7b000048/
#
# Description: 
# Detect whether a given string is a pangram (containing every letter of the alphabet, regardless of case).  Return True for pangrams.  
#
# Approach:
# Iterate through each character in an alphabet string and return False if the character is not found.  After all characters, return True.  

def is_pangram(st):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    for ch in alpha:
        if ch not in st.lower():
            return False
    return True