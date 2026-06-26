class Solution:
    def isValid(self, s: str) -> bool:
        valid = {
            '(' : ')',
            '[' : ']',
            '{' : '}'
        }
        stack = []
        for p in s:
            if p in valid.keys():
                stack.append(p)
            else:
                if not stack:
                    return False
                if p != valid[stack.pop()]:
                    return False
        if not stack:
            return True
        return False