
#pushed = [1,2,3,4,5]
#popped = [4,5,3,2,1]
class Solution:
    def validateStackSequences(self, pushed, popped) -> bool:
        stack = []
        l = 0
        for i in range(len(pushed)):
            stack.append(pushed[i])

            while stack and stack[-1]  == popped[l]:
                l += 1
                stack.pop()
        return not stack

pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
solution = Solution()
print(solution.validateStackSequences(pushed, popped))

    