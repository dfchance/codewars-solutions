# Kata: Shortest Word
# Difficulty: 7 kyu
#
# Description: 
# Find the shortest word in a given string and return its length.
#
# Approach:
# Iterate through the string, checking each word.  If it shorter than the previously identified shortest word, save the value. 

def find_short(string):
    # Split the string so it can be evaluated word by word
    string = string.split()
    
    # Start with the first word
    word = string[0]
    
    # Index of the next word to be compared
    n = 1
    
    # Number of words in the string
    l_str = len(string)
    
    # Get the length of the first word
    l = len(word)
    
    # Iterate through all the words
    while n < l_str:
        word = string[n]
        if len(word) < l:
            l = len(word)
        n += 1
    return l