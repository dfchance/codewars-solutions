# Kata: Break Camel Case
# Difficulty: 6 kyu
# URL: https://www.codewars.com/kata/5208f99aee097e6552000148
#
# Description: 
# Take an a camel case string and return the string with spaces between the words.  
#

# Original Solution from May 13, 2026
# Approach:
# Iterate through the word and insert spaces when uppercase letters are found. 

def solution(string):
    l = len(string)
    n = 0
    while n < l: 
        if string[n].isupper(): 
            string = string[0:n] + " " + string[n:]
            print(string[n])
            n += 1
        n += 1
        print("outside if: " + string[n])
    return string    

# Refactored Solution from June 4, 2026
# Approach:
# Use a for loop to create a new string inserting spaces ahead of uppercase letters. 
def solution(string):
    str = ""
    for l in string:
        if l.isupper():
            str += " "
        str += l
    return str