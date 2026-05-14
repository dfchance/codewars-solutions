# Kata: Categorize New Member
# Difficulty: 7 kyu
# URL: https://www.codewars.com/kata/5502c9e7b3216ec63c0001aa
#
# Description: 
# Categorize new members of a croquet club as "Open" or "Senior".  To be a senior, a member must be at least 55 years old and have a handicap greater than 7.
#
# Approach:
# Iterate through the data checking each members age and handicap.  Append either "Open" or "Senior" to a list of members based on their data. 

def open_or_senior(data):
    open = "Open"
    senior = "Senior"
    members = []
    n = 0
    while n < len(data):
        if data[n][0] < 55:
            members.append(open)
        elif data[n][0] >= 55:
            if data[n][1] > 7:
                members.append(senior)
            else:
                members.append(open)
        n += 1
    return members