from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = defaultdict(int)
        left = 0
        answer = 0
        for right in range(len(s)):
            counts[s[right]] += 1
            maxamt = max(counts.values())
            while right - left + 1 - maxamt > k:
                counts[s[left]]-=1
                left += 1
                maxamt = max(counts.values())
            answer = max(right - left + 1, answer)
        return answer

            

