from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = defaultdict(list)
        answer = []
        for word in strs:
            sort = tuple(sorted(word))
            hash[sort].append(word)
        for val in hash.values():
            answer.append(val)
        return answer