from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        valid = set()
        left = 0
        answer = 0
        for right in range(len(s)):
            while s[right] in valid:
                valid.remove(s[left])
                left +=1
            valid.add(s[right])
            answer = max(right - left + 1, answer)
        return answer