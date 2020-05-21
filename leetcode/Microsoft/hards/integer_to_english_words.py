"""
273. Integer to English Words
Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 231 - 1.

Example 1:

Input: 123
Output: "One Hundred Twenty Three"
Example 2:

Input: 12345
Output: "Twelve Thousand Three Hundred Forty Five"
Example 3:

Input: 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
Example 4:

Input: 1234567891
Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"
"""

map_one = {
    0: "",
    1: "One ",
    2: "Two ",
    3: "Three ",
    4: "Four ",
    5: "Five ",
    6: "Six ",
    7: "Seven ",
    8: "Eight ",
    9: "Nine ",            
}

map_two = {
    2: "Twenty ",
    3: "Thirty ",
    4: "Forty ",
    5: "Fifty ",
    6: "Sixty ",
    7: "Seventy ",
    8: "Eighty ",
    9: "Ninety "
}

map_two_special = {
    0: "Ten ",
    1: "Eleven ",
    2: "Twelve ",
    3: "Thirteen ",
    4: "Fourteen ",
    5: "Fifteen ",
    6: "Sixteen ",
    7: "Seventeen ",
    8: "Eighteen ",
    9: "Nineteen ",
}

def one(num: int) -> str:
    return map_one[num]
def two(num: int) -> str:
    div = num//10
    if div == 0:
        return one(num%10)
    if div == 1:
        return map_two_special.get(num%10, "")
    if div > 1:
        return map_two[div] + one(num%10)


def three(num: int) -> str:
    if num==0:
        return ""

    div = num //100

    if div == 0:
        return two(num%100)
    return one(div) + "Hundred " + two(num%100) 

class Solution:
    def numberToWords(self, num: int) -> str:       
        if num ==0:
            return "Zero"
        billion = num//10**9
        million = (num%10**9)//10**6
        thousand = (num%10**6)//10**3
        
        res = ""
        if(billion > 0):
            res += three(billion) + "Billion "
        if(million > 0):
            res += three(million) + "Million "
        if(thousand > 0):
            res += three(thousand) + "Thousand "
        res+= three(num%1000)
        
        
        return res.strip()
            
        
s=Solution()
input=1234567
expected="One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
output= s.numberToWords(input)
print('input %s:'% input)
print('Output %s:'% output)
print('Expected: %s'% expected)
print('passed: %s'% (output==expected))