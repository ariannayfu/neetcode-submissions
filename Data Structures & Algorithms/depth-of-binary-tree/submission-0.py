# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        def findDepth(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            lDepth = findDepth(node.left)
            rDepth = findDepth(node.right)
            return 1 + max(lDepth, rDepth)
        return findDepth(root)
        