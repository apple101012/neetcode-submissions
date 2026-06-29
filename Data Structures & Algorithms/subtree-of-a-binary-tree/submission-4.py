# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        
        curr = self.sameTree(root, subRoot)
        if curr:
            return True
        left = self.isSubtree(root.left, subRoot)
        right = self.isSubtree(root.right, subRoot)
        return left or right 
    def sameTree(self, n1, n2):
        if not n1 and not n2:
            return True
        elif n1 and n2 and n1.val == n2.val:
            s1 = self.sameTree(n1.left, n2.left)
            s2= self.sameTree(n1.right, n2.right)
            return s1 and s2
        else:
            return False
        
            
            