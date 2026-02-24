# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def dfs(node, value=0):
            if not node:
                return 0
            
            value = (value << 1) | node.val
            
            if not (node.left or node.right):
                return value
            
            return dfs(node.left, value) + dfs(node.right, value)
        
        return dfs(root)