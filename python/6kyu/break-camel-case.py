# Kata: Break Camel Case
# Difficulty: 6 kyu
#
# Description: 
# Take an a camel case string and return the string with spaces between the words.  
#
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