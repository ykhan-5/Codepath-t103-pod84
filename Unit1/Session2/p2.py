#U --> Understand Should we use Map or DICT?
# Are there any Edge cases?
#I/O --> I==Str and O =Int
# Uppercase and Lowercases
#If the first number is smaller than second number, we have to substract
# for example: MCM = 1000 - 100 + 1000

#M --> Match --> HashMap, 
#P
#I
#R
#E
class Solution:
    def RomanToInt(self, s: str):
        total = 0
        map = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        for i in range(len(s)):
            if i+1<len(s) and map[s[i]] >= map[s[i+1]]:
                total += map[s[i]]
            
            elif i+1<len(s) and map[s[i]] < map[s[i+1]]:
                total -= map[s[i]]
            
            else:
                total += map[s[i]]
        return total

s = "III"
solution = Solution()
print(solution.RomanToInt(s))

    