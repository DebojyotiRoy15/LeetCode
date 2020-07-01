#https://leetcode.com/problems/minimum-depth-of-binary-tree/

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        else:
            p = self.minDepth(root.left)
            q = self.minDepth(root.right)
            if p == 0 or q == 0:
                return max(p + 1, q + 1)
            return min(p + 1, q + 1)
