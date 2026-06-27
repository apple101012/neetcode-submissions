import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxp = max(piles)
        left = 1
        right = maxp
        answer = maxp
        while left <= right:
            mid = (left + right) // 2
            temp = 0
            for p in piles:
                temp += math.ceil(p / mid)
            if temp <= h:
                answer = min(mid, answer)
                right = mid - 1
            else: 
                left = mid + 1
        return answer
