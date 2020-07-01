#https://leetcode.com/problems/invert-binary-tree/

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        stack = []
        stack.append(root)
        while stack:
            v = stack.pop()
            if v:
                v.left, v.right = v.right, v.left 
                stack.append(v.left)
                stack.append(v.right)
        return root
