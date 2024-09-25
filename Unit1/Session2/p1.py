class Solution:
    # def integerReplacement(self, n: int, memo = {}) -> int:
    def integerReplacement(self, n: int) -> int:
        return self.helper(n)
      

    def helper(self, n):
        if n == 1:
          # memo[n] = 0
          return 0
        
        # if n not in memo:
          # if odd 
        if n % 2 != 0:
          # memo[n] = 1 + min(self.integerReplacement(n-1, memo), self.integerReplacement(n+1, memo))
          return 1 + min(self.integerReplacement(n-1), self.integerReplacement(n+1))
          
          # if even
        else:
          # memo[n] = 1 + self.integerReplacement(n//2, memo)
          return 1 + self.integerReplacement(n//2)


      
input = 7
solution = Solution()
print(solution.integerReplacement(input))
