# String Rotation; Assume you have a method isSubstring which checks if one word is a substring
# of another. Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one
# call to isSubstring [e.g., "waterbottle " is a rotation of 'erbottlewat"),

# from a rotation ponint we can break the s1 into xy => s1 = xy so we want the s2 to be yx
# yx will always be a substring of xyxy => s2 should be a substring of s1+s1 otherwise s2 is not a roatation of s1
   
def is_rotation(s1: str, s2: str) -> bool:
    res = s2 in s1+s1 if len(s1) == len(s2) and len(s1) > 0 else False
    print("%s is rotation of %s: %s"%(s2, s1, res))

def solve():
    is_rotation("waterbottle","erbottlewat")
    is_rotation("abcd","cdab")
    is_rotation("adcb","cdab")