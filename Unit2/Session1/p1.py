# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
         
class Solution:
    def swapPairs(self, head):
        if not head or not head.next:
            return head
        
        dummy = ListNode(0)    
        dummy.next=head
        
        first = head
        second = head.next
        temp = dummy
        
        while first and second:
            temp.next = second
            temp = temp.next
            first.next = second.next
            second.next = first #temp.next = first
            temp = temp.next
            first = first.next
            if first:
                second = first.next

        if first:
            temp.next = first

        return dummy.next

        


s = "III"
solution = Solution()
print(solution.func(s))

#1st pointer
#2nd pointer

#dummy node + tail pointer;

#base cases:
# empty || head.next empty -> return list