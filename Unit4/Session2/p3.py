class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def arrayToLinkedList(nums):
    if not nums:
        return None
    head = ListNode(nums[0])
    current = head
    for num in nums[1:]:
        current.next = ListNode(num)
        current = current.next
    return head

def printLinkedList(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

class Solution:
    def partitionList(self, head: ListNode, x: int) -> ListNode:
        # Setup for solving the partition logic
        # Add your code here
        pass

# Test input
nums = [1, 4, 3, 2, 5, 2]
x = 3

head = arrayToLinkedList(nums)

solution = Solution()
new_head = solution.partitionList(head, x)

printLinkedList(new_head)
