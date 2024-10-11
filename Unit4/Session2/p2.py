#I
#M: sorting, splitting, joining
#P: sort each, make them a key, value match and output in seperate arrays 
#I
#R
#E


class Solution:
    
    def groupAnagrams(self, strs):
        sortedKeys = {}

        for s in strs:
            key =  "".join(sorted(s))
            if key not in sortedKeys:
                sortedKeys[key] = []
            
            sortedKeys[key].append(s)

        return sortedKeys.values()


            
strs = ["eat","tea","tan","ate","nat","bat"]
solution = Solution()
print(solution.groupAnagrams(strs))
