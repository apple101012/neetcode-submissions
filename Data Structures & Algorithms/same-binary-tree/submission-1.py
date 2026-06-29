# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(one, two):
            if not one and not two:
                return True
            if not one and two:
                return False
            if not two and one:
                return False
            left = dfs(one.left, two.left)
            right = dfs(one.right, two.right)

            return left and right and one.val == two.val
        answer = dfs(p, q)
        return answer