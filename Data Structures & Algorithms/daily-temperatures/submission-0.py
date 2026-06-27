class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        answer = [0] * len(temperatures)
        for index, val in enumerate(temperatures):
            if not stack:
                stack.append([val, index])
            else:
                while(stack and val > stack[-1][0]):
                    prev = stack[-1][1]
                    answer[prev] = index - prev
                    stack.pop()
                stack.append([val, index])
            
        return answer
                    

