class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        keys = {}
        for i in nums:
            if i not in keys:
                keys[i] = 1
            else:
                keys[i] += 1
        for nums in keys:
            if keys[nums] > 1:
                return True
        return False
        
        