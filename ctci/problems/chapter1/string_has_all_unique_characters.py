# Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
# cannot use additional data structures?


def isUniqieUsingHashSet(input):
    mem = set()
    for char in input:
        if ord(char) in mem:
            print(False)
            return False
        mem.add(ord(char))
    print(True)
    return True

def isUniqueWithoutAdditionalDataStructure(input):
    checker = 0
    for c in input:
        val = ord(c) - ord('a')
        if checker & (1 << val) > 0:
            print(False)
            return False
        checker |= (1 << val)
    print(True)
    return True

def solve():
    input = "bc"
    isUniqieUsingHashSet(input)
    isUniqueWithoutAdditionalDataStructure(input)
