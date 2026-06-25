class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * (len(nums))
        # building my solution 
        for i in range(1, len(nums)):
            result[i] = result[i-1] * nums[i - 1]
        post = [1] * len(nums)
        for i in range(len(nums) - 2, -1, -1):
            post[i] = post[i + 1] * nums[i + 1]
        return [result[i] * post[i] for i in range(len(nums))] 

        