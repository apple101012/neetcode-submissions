class Solution:
    def trap(self, height: List[int]) -> int:
        answer = 0
        left = 0
        right = len(height) - 1
        leftmin = float("-inf")
        rightmin = float("-inf")
        while(left < right):
            leftmin = max(height[left], leftmin)
            rightmin = max(height[right], rightmin)
            if(leftmin < rightmin):
                attempt = leftmin - height[left]
                if(attempt > 0):
                    answer += attempt
                left+=1
            else:
                attempt = rightmin - height[right]
                if (attempt > 0):
                    answer += attempt
                right -=1
    
        return answer


        
            