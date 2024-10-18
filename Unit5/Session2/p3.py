# Forgot to say : Nice meeting you all.
#U: 
#M: 
#P: 
#I
#R
#E: 

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import defaultdict
def levelorder(root: TreeNode) -> int:
    # Prepare
    vertical_ax = defaultdict(list)
    
    #call dfs
    dfs(root, 0)


    def dfs(root, x):
        # check
        if not root:
            return None
        # visit node
        vertical_ax[x].append(root.val)
        # dfs
        dfs(root.left, x - 1)
        dfs(root.right, x + 1)

    # Result
    res = []
    # for key_val in vertical_ax.keys():
    #     res.append(vertical_ax[key_val])
    return vertical_ax.values()

# Example to help you test
def create_example_tree():
    
    return TreeNode(3, 
                    TreeNode(9, None, None), 
                    TreeNode(20, 
                             TreeNode(15, None, None), TreeNode(7, None, None)))

root = create_example_tree()

result = prulevelorderne(root)
print(result) 


