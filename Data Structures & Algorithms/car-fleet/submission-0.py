class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        group = []
        for x, y in zip(position, speed):
            group.append((x, y))
            group.sort(reverse=True)
        stack = []
        def time(val):
            return (target - val[0]) / val[1]
        for i in range(len(speed)):
            if not stack:
                stack.append(group[i])
            else:
                if(time(group[i]) > time(stack[-1])):
                    stack.append(group[i])
        return len(stack)
                