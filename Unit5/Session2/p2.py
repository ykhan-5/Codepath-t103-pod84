# Definition for a binary tree node.

#U: 
#M: recursion
#P: base case: 0 with no child
#I
#R
#E: 

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def prune(root: TreeNode) -> int:
    if not root:
        return None
    
    #recursive first
    root.left = self.prune(root.left)
    root.right = self.prune(root.right)

    if not root.right and not root.left and root.val == 0:
        return None

    return root

# Example to help you test
def create_example_tree():
    
    return TreeNode(3, 
                    TreeNode(9, None, None), 
                    TreeNode(20, 
                             TreeNode(15, None, None), TreeNode(7, None, None)))

root = create_example_tree()

result = prune(root)
print(result) 
