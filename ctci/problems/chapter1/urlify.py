# URLify: Write a method to replace all spaces in a string with '%20'.
# You may assume that the string has suffcient space at the end to hold
# the additional characters and that you are given the "true" length of the string.
# Example:
# Input: "Mr 3ohn Smith             13
# Output: "Mr%203ohn%20Smith"
from typing import List

def replaceSpaces(str: List[str], length) -> str:
        """
        strType: list[str]
        """
        count = 0
        for i in range(length):
            if str[i] == ' ':
                count += 1
        # the number of spaces is count, length - count: # of chars 
        index = length + count*2
        for i in range(length - 1, 0, -1):
            if str[i] == " ":
                str[index-1] = "0"
                str[index-2] = "2"
                str[index-3] = "%"
                index -= 3
            else:
                str[index-1]   = str[i]
                index -= 1
        res = ""        
        return res.join(str)

def urlify(s: List[str], trueLength: int) -> str:
    copy_of_s = s.copy()
    i = 0
    j = 0
    while j < trueLength:
        if copy_of_s[j] == " ":
            s[i] = '%'
            s[i+1] = '2'
            s[i+2] = '0'
            i += 3
        else:
            s[i] = copy_of_s[j]
            i += 1 
        j+=1
    res = ""
    return res.join(s)

def solve():
    res = urlify(list("Mr 3ohn Smith    "), 13)
    res1 = replaceSpaces(list("Mr 3ohn Smith    "), 13)
    print(res)
    print(res1)
    print(res == res1)
    return res