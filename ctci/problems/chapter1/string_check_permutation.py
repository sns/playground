# Check Permutation: Given two strings. Write a method to decide if one is a permutation of the other

def getCharCountMap(input: str):
    char_count_map = {}
    for i in input:
        if ord(i) in char_count_map:
            char_count_map[ord(i)] += 1
        char_count_map[ord(i)] = 1
    return char_count_map

def solve():
    input1 = "sinas"
    input2 = "aniss"
    if len(input1) != len(input2):
        print(False)
        return False
    input1_char_map = getCharCountMap(input1)
    input2_char_map = getCharCountMap(input2)
    print(input1_char_map == input2_char_map)
    return input1_char_map == input2_char_map

