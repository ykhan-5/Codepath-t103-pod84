#U: n is cooldown time
#M: hashmaps (x2) 1 for cooldown, 1 for counting
#P: Build the count hashmap

#count = {}
#cooldown = {}
#numIntervals = 0
# for t in tasks:
# count[t] += 1
# cooldown[t] = 0

# while count:
# 
# for t in count:







#I
#R
#E

from collections import Counter
import heapq
class Solution:
    
    def schedule(self, tasks):
        
        count = Counter(tasks) # A:3 and B:3
        
        max_heap = [-count for count in count.values()]
        print(max_heap)
            
    

tasks = ["A","A","A","A","B","B","B"]
solution = Solution()
print(solution.schedule(tasks))
