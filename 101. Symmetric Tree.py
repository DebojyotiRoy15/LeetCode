#https://leetcode.com/problems/symmetric-tree/

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.Aux(root, root)
    
    def Aux(self, t1, t2):
        if t1 is None and t2 is None:
            return True
        elif t1 is None or t2 is None:
            return False
        else:
            p = self.Aux(t1.left, t2.right)
            q = self.Aux(t1.right, t2.left)
            return (t1.val == t2.val) and p and q
