# U: 
# M: Two Pointer?
# P: 
# l. r = 0, len(s)
# while l < r:

# check is s[l] or s[r] a letter
# isalpha() or skip

# check is s[l].lower() == s[r].lower() 
    #if nto return false

#at end return True




class Solution:
    
    def palindrome(self, s): 
        l, r = 0, len(s) - 1    

        while l < r:
            if not s[l].isalnum():
                l += 1
            
            elif not s[r].isalnum():
                r -= 1
            
            else:
                if s[l].lower() != s[r].lower():
                        return False
                    
                l += 1
                r -= 1

        return True


s = "malayalam"
solution = Solution()
print(solution.palindrome(s))
