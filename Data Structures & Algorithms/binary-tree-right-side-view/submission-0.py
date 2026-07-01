# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = []
        answer = []
        queue.append(root)
        while queue:
            right = None
            level = len(queue)
            for i in range(level):
                curr = queue.pop(0)
                if curr:
                    right = curr
                    queue.append(curr.left)
                    queue.append(curr.right)
            if right:
                answer.append(right.val)
        return answer


        