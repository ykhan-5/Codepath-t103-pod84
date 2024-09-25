# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
         
class Solution:
    def swapPairs(self, head, k):
        if not head or not head.next or k == 0:
            return head

        temp = head
        size = 0

        #lwn(head) idea
        while temp:
            size += 1
            temp = temp.next


        # Remainder
        newK = k % size

        if newK == size or newK == 0:
            return head

        # len(head)-remainder
        numiteration = size - newK - 1

        beforeNewHead = head
        
        #newHead to iterated node
        while numiteration > 0:
            numiteration -= 1
            beforeNewHead = beforeNewHead.next
            #ex. at 4

        newHead = beforeNewHead.next

        beforeNewHead.next = None
        end = newHead

        while end and end.next:
            end = end.next
        
        end.next = head

    
        return newHead

        


s = "III"
solution = Solution()
print(solution.func(s))

    # rotate module of size 