#https://leetcode.com/problems/cousins-in-binary-tree

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        q = [root]
        parent = {}
        parent[root.val] = 0
        depth =  {}
        depth[root.val] = 0
        while len(q) > 0:
            s = q.pop(0)
            if s.left:
                q.append(s.left)
                depth[s.left.val] = depth[s.val] + 1
                parent[s.left.val] = s.val
            if s.right:
                q.append(s.right)
                depth[s.right.val] = depth[s.val] + 1
                parent[s.right.val] = s.val
        if depth[x] == depth[y]:
             if  parent[x] != parent[y]: 
                return True
        else:
            return False
