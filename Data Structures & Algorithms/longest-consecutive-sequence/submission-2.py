class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if(len(nums) == 0):
            return 0
        nums.sort()
        answer = 1
        curr = 1
        for i in range(1, len(nums)):
            if(nums[i] == nums[i - 1]):
                continue
            if nums[i] == nums[i - 1] + 1:
                curr+=1
            else:
                curr = 1
            answer = max(curr, answer)
        return answer