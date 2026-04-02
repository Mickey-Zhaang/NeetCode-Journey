# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.unb = 0

        def dfs(root, flag):
            if not root:
                return 0

            if flag == -1:
                return -1

            h_l = dfs(root.left, flag)
            h_r = dfs(root.right, flag)

            if abs(h_l - h_r) > 1:
                flag = -1
            else:
                flag = max(h_l, h_r) + 1
            
            return flag

        self.unb = dfs(root, self.unb)

        return False if self.unb == -1 else True