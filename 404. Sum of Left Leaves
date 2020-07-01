#https://leetcode.com/problems/sum-of-left-leaves/
#DFS

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        sum = 0
        if root is None:
            return sum
        else:
            stack = []
            stack.append(root)
            while stack:
                v = stack.pop()
                if v.left:
                    stack.append(v.left)
                    if v.left.left is None and v.left.right is None:
                        sum = sum + v.left.val
                if v.right:
                    stack.append(v.right)
            return sum
