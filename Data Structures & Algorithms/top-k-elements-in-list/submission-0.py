from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        freq = [[] for i in range(len(nums) + 1)]
        answer= []
        for num in nums:
            count[num] +=1
        for num, amt in count.items():
            freq[amt].append(num)
        
        for i in range (len(freq) - 1, 0, -1):
            for num in freq[i]:
                answer.append(num)
                if(len(answer) == k):
                    return answer