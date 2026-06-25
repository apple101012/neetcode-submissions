class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for index, val in enumerate(nums):
            num = target - val
            if num in hash:
                return [hash[num], index]
            hash[val] = index