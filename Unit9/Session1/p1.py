class Solution:
    def longestPalindrome(s):
        if not s:
            return ""
        
        start = 0
        end = 0

        def expandPalindrome(s, left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            return right - left - 1

        for i in range(len(s)):
            both_sides = expandPalindrome(s, i, i)
            one_side = expandPalindrome(s, i, i + 1)
            max_len = max(both_sides, one_side)

            if max_len > (end - start + 1):

                start = i - (max_len - 1) // 2
                end = i + max_len // 2

        return s[start:end+1]
            
        
        
            
    

s = "babad"
solution = Solution()
print(solution.longestPalindrome(s))
s = "bbc"
solution = Solution()
print(solution.longestPalindrome(s))