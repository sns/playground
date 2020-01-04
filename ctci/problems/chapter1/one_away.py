# One Away: There are three types of edits that can be performed on strings: insert a character,
# remove a character, or replace a character. Given two strings, write a function to check if they are
# one edit (or zero edits) away.
# EXAMPLE
# pale , pie -> true
# pales , pale -> true
# pale , bale -> true
# pale , bake -> false

def isOneWay(s1: str, s2: str) -> bool:
    m = len(s1)
    n = len(s2)

    if abs(m - n) > 1:
        return False
    i = 0
    j = 0
    count = 0
    while i < m and j < n:
        if s1[i] != s2[j]:
            if count == 1:
                return False
            count += 1
            if m > n:
                i += 1
            elif n > m:
                j += 1
            else:
                i += 1
                j += 1
        else:
            i += 1
            j += 1
    
    if i < m or i < n:
        count += 1
    
    return count <= 1

# Returns true if edit distance between s1 and s2 is 
# one, else false 
def isOneWay1(s1, s2): 
  
    # Find lengths of given strings 
    m = len(s1) 
    n = len(s2) 
  
    # If difference between lengths is more than 1, 
    # then strings can't be at one distance 
    if abs(m - n) > 1: 
        return False 
  
    count = 0    # Count of isEditDistanceOne 
  
    i = 0
    j = 0
    while i < m and j < n: 
        # If current characters dont match 
        if s1[i] != s2[j]: 
            if count == 1: 
                return False 
  
            # If length of one string is 
            # more, then only possible edit 
            # is to remove a character 
            if m > n: 
                i+=1
            elif m < n: 
                j+=1
            else:    # If lengths of both strings is same 
                i+=1
                j+=1
  
            # Increment count of edits 
            count+=1
  
        else:    # if current characters match 
            i+=1
            j+=1
  
    # if last character is extra in any string 
    if i < m or j < n: 
        count+=1
  
    return count == 1

            
    
        
def solve():
    print(isOneWay("pale", "ple"))
    print(isOneWay1("pale", "ple"))
    print(isOneWay("pales", "pale"))
    print(isOneWay1("pales", "pale"))
    print(isOneWay("pales", "bale"))
    print(isOneWay1("pales", "bale"))
    print(isOneWay("pale", "bale"))
    print(isOneWay1("pale", "bale"))
    print(isOneWay("pale", "bake"))
    print(isOneWay1("pale", "bake"))