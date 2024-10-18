# Definition for a binary tree node.

#U: recursion, stack - dosbol
#M: recursion
#P: take min of recursive call each time, base case = no children
#I
#R
#E: O(N), O(N) space

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def minDepth(root: TreeNode) -> int:
    if not root:
        return 0
    if not root.right and not root.left:
        return 1
    if not root.right:
        return 1 + self.minDepth(root.left)
    if not root.left:
        return 1 + self.minDepth(root.right)
    
    return 1 + min(self.minDepth(root.right), self.minDepth(root.left))

# Example to help you test
def create_example_tree():
    
    return TreeNode(3, 
                    TreeNode(9, None, None), 
                    TreeNode(20, 
                             TreeNode(15, None, None), TreeNode(7, None, None)))

root = create_example_tree()

result = minDepth(root)
print(result) 
