#U: No duplicate triplets + 3 numbers add to 0 / should we keep the order of numbers??
#M: 
#P
#I
#R
#E


class Solution:
    
    def ThreeSum(self, nums):
        res = set()
        nums.sort()
        print(nums)
        seen = set()

        for i in range(len(nums)):
            
            k = i + 1
            z = len(nums) - 1

            while k < z:

                if nums[k] + nums[z] + nums[i] == 0:
                    res.add((nums[i], nums[k], nums[z]))

                if nums[k] + nums[z] + nums[i] > 0:
                    z -= 1
                else:
                    k += 1

        return list(res)



        
        
        
        # res = set()
        
        # nums.sort()
        
        # for i in range(len(nums)):
        #     for j in range(1, len(nums)):
        #         for z in range(2, len(nums)):
        #             if i != j and j != z and i != z:
        #                 if nums[i] + nums[j] + nums[z] == 0:
        #                     res.add([nums[i],nums[j],nums[z]])

        # return list(res)
    

nums = [-1,0,1,2,-1,-4]
solution = Solution()
print(solution.ThreeSum(nums))
