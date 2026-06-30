# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        answer = []
        queue = []
        queue.append(root)
        while queue:
            nums = []
            for k in range(len(queue)):
                curr = queue.pop(0)
                if curr:
                    nums.append(curr.val)
                    queue.append(curr.left)
                    queue.append(curr.right)
            if nums:
                answer.append(nums)
        return answer
