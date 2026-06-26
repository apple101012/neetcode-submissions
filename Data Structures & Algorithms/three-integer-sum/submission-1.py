class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        answer = []
        for i in range(len(nums)):
            a = nums[i]
            if nums[i] > 0:
                continue
            if not i == 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                b = nums[left]
                c = nums[right]
                curr = a + b + c
                if curr == 0:
                    if [a,b,c] not in answer:
                        answer.append([a, b, c])
                    right-=1
                    left+=1
                elif(curr > 0):
                    right -= 1
                else:
                    left += 1
        return answer
