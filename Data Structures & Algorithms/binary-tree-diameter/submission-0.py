# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.maxDiameter = 0
        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            
            leftHeight = dfs(node.left)
            rightHeight = dfs(node.right)

            self.maxDiameter = max(self.maxDiameter, leftHeight + rightHeight)
            return 1 + max(leftHeight, rightHeight)
        dfs(root)
        return self.maxDiameter
