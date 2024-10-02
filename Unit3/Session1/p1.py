class Solution:
    
    def mostWater(self, height):
        l, r = 0, len(height) - 1

        maxArea = 0

        while l < r:
            area = min(height[l], height[r]) * (r-l)

            maxArea = max(area, maxArea)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return maxArea
            
    

height = [1,8,6,2,5,4,8,3,7]
solution = Solution()
print(solution.mostWater(height))
