class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        op = []
        for t in tokens:
            if t == '+':
                nums.append(int(nums.pop() + nums.pop()))
            elif t == '*':
                nums.append(int(nums.pop() * nums.pop()))
            elif t == '/':
                second = nums.pop()
                first = nums.pop()
                nums.append(int(first / second))
            elif t == '-':
                second = nums.pop()
                first = nums.pop()
                nums.append(int(first - second))
            else:
                nums.append(int(t))
        return nums.pop()
                