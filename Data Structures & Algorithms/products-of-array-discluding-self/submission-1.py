class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre = [1] * n
        post = [1] * n

        product = 1

        for i in range(n):
            pre[i] = product
            product *= nums[i]
        
        product = 1
        for i in range(n-1,-1,-1):
            post[i] = product
            product *= nums[i]

        result = [1]*n

        for i in range(n):
            result[i] = pre[i] * post[i]

        return result 