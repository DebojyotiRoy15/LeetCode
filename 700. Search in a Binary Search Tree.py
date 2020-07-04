#https://leetcode.com/problems/search-in-a-binary-search-tree/

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        while root:
            if root.val == val :
                return root
            elif val < root.val:
                root = root.left
            elif val > root.val:
                root = root.right
        return None
