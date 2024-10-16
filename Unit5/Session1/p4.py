#U
#M - stack, compare top values, larger abs() stays
#P - append the asteroids one at a time, when we see different sign, we compare, keep the "larger" one
# also [10, 2, -1000] -> [100, -1000] -> [-1000]
#I
#R
#E

class Solution:
    def asteroidCollision(self, asteroids):
        stack = []

        for asteroid in asteroids:
            if not stack:
                stack.append(asteroid)

            while stack[-1] * asteroid < 0:
                if abs(stack[-1]) > abs(asteroid):
                    flag = False
                    continue
                elif abs(stack[-1]) < abs(asteroid):
                    stack.pop()
                    flag = True
                else:
                    stack.pop()
                    flag = False

            if flag:
                stack.append(asteroid)


        return stack

        
asteroids = [5,10,-5]
solution = Solution()
print(solution.asteroidCollision(asteroids))