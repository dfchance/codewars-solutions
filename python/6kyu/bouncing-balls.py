# Kata: Bouncing Balls
# Difficulty: 6 kyu
# URL: https://www.codewars.com/kata/5544c7a5cb454edb3c000047
# 
# Description: 
# Given the parameters height, window (height) and bounce (factor), calculate the number of times a ball dropped from a certain height will be seen bouncing up and down before it ceases.  
#
# Approach:
# Check length of array and return the appropriate concatenated string using if statements. 

def bouncing_ball(height, bounce, window):
    # Check that parameters pass requirements
    if height <= 0 or 0 <- bounce or bounce >= 1 or window >= height:
        # Error code
        return -1
    else: 
        seen = 1
        while height >= window:
            height *= bounce
            if height > window:
                # Ball is seen going up, and coming back down (2x)
                seen += 2
            else:
                return seen
