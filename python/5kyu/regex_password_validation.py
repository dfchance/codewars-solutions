# Kata: Regex Password Validation
# Difficulty: 5 kyu
# URL: https://www.codewars.com/kata/52e1476c8147a7547a000811
# 
# Description: 
# Write a regex to validate a password that only accepts alphanumeric characters, requires one number, one uppercase and one lowercase and must be at least 6 characters long.  
#
# Approach:
# Check for the three required formats, confirm no other characters are present, check for length.  

regex="(?=.*[0-9])(?=.*[A-Z])(?=.*[a-z])(?!.*\s)(?!.*[^a-zA-Z0-9]).*.{6,}"
