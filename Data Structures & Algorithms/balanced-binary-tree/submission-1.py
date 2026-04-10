# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return 0

            l_height = dfs(root.left) + 1
            r_height = dfs(root.right) + 1

            return max(l_height, r_height)
        
        if not root:
            return True
        
        l_height = dfs(root.left)
        r_height = dfs(root.right)

        print(l_height)
        print(r_height)

        if abs(l_height - r_height) > 1:
            return False
        return True 



        