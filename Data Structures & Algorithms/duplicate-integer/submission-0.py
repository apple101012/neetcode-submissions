from collections import defaultdict
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash = defaultdict(list)
        for num in nums:
            hash[num].append(num)
            if len(hash[num]) > 1:
                return True
        return False