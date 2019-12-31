# Palindrome Permutation: Given a string,
# write a function to check if it is a permutation of a palindrome. 
# A palindrome is a word or phrase that is the same forwards and backwards. 
# A permutation is a rearragement of letters. 
# The palindrome does not need to be limited to just dictionary words. 

# Example:
    # Input: "Tact Coa"
    # Output: True (permutations: "taco cat", "atco eta", etc.)

def checkForPalidromePermutation(str: str):
    char_map = []
    for i in range(26):
        char_map.append(0)
    for char in str:
        if char != " ":
            char_map[ord(char.lower()) - ord('a')] += 1
    number_of_characters_with_odd_count = 0
    for count in char_map:
        number_of_characters_with_odd_count += count % 2
    
    return number_of_characters_with_odd_count <= 1

def solve():
    str = "Tact Coa"
    res = checkForPalidromePermutation(str) 
    print(res)
    return res

