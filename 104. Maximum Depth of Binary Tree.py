#https://leetcode.com/problems/maximum-depth-of-binary-tree/

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        else:
            l = self.maxDepth(root.left)
            r = self.maxDepth(root.right)
            
            return max(l + 1, r + 1)
