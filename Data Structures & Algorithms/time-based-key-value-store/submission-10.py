from collections import defaultdict
class TimeMap:

    def __init__(self):

        self.main = defaultdict(list)


    def set(self, key: str, value: str, timestamp: int) -> None:
        self.main[key].append([timestamp, value])
        
            

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.main:
            return ""
        group = self.main[key]
        left = 0
        right = len(group) - 1
        while left <= right:
            mid = (left + right) // 2
            time = group[mid][0]
            if time == timestamp:
                return group[mid][1]
            if time > timestamp:
                right = mid - 1
            else:
                left = mid + 1
        if(right < 0):
            return ""
        return group[right][1]
        
