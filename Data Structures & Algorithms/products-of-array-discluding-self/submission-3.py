class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre = [1] * n
        pos = [1] * n
        result = [1] * n

        product = 1

        for i in range(n):
            pre[i] = product
            product *= nums[i]

        product = 1
        for i in range(n-1, -1, -1):
            pos[i] = product
            product *= nums[i]

        for i in range(n):
            result[i] = pre[i] * pos[i]
        return result        