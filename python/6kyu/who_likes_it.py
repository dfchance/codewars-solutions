# Kata: Who Likes It?
# Difficulty: 6 kyu
# URL: https://www.codewars.com/kata/5266876b8f4bf2da9b000362
# 
# Description: 
# Take an array of names an dreturn a string containing the names and the phrase "likes this." 
#
# Approach:
# Check length of array and return the appropriate concatenated string using if statements. 

def likes(names):
    num_likes = len(names)
    
    if num_likes == 0:
        return "no one likes this"
    if num_likes == 1:
        return names[0] + " likes this"
    if num_likes == 2:
        return names[0] + " and " + names[1] + " like this"
    if num_likes == 3:
        return names[0] + ", " + names[1] + " and " + names[2] + " like this"
    if num_likes > 3: 
        return names[0] + ", " + names[1] + " and " + str(num_likes - 2) + " others like this"