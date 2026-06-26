class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1 = sorted(s1)
        k = len(s1)
        left = 0
        for right in range(len(s2)):
            diff = right - left + 1 
            if(diff == k):
                if(sorted(s2[left:right + 1]) == s1):
                    return True
                else:
                    left+=1
        return False

            
                
        