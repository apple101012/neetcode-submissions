# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if p.val == root.val or q.val == root.val:
            return root
        while root:
            val = root.val
            p1 = p.val
            q1 = q.val
            if (q1 < val and p1 > val) or (q1 > val and p1 < val) or (p1 == val) or (q1 == val):
                return root
            elif q1 > val and p1 > val:
                root = root.right
            else:
                root = root.left