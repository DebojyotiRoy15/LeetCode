#https://leetcode.com/problems/path-sum/

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root is None :
            return False
        
        else:
            p = self.hasPathSum(root.left, sum - root.val)
            q = self.hasPathSum(root.right, sum - root.val)
            if root.val == sum and root.left is None and root.right is None:
                return True
            return p or q
