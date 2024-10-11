#M: Set and sliding window (l, r)
#P
# iterate one by one till the right pointer is at the end
# add to set if not seen, 
# if it in the set -> move left until repeated char no longer present

#return max window length




class Solution:
    
    def longestSub(self, s):
        l, r = 0, 0 
        seen = set()
        maxlength = 0

        while r < len(s):
            if s[r] not in seen:
                seen.add(s[r])
                print("Adding", s[r])
                r += 1
                maxlength = max(maxlength, r - l)
            else:
                seen.remove(s[l])
                l += 1

        return maxlength

            
    
s = "abcabcbb" # input
# s = "yabcatw"
solution = Solution()
print(solution.longestSub(s))
