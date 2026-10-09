class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre = [1] * n
        pos = [1] * n
        result = [1]*n

        value = 1
        for i in range(n):
            pre[i] = value
            value *= nums[i]
        
        value = 1
        for i in range(n-1, -1, -1):
            pos[i] = value
            value *= nums[i]

        for i in range(n):
            result[i] = pre[i] * pos[i]
        return result