class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        keys = {}
        for i in nums:
            if i not in keys:
                keys[i] = 1
            else:
                keys[i] += 1
        for duplicate in keys:
            if keys[duplicate] > 1:
                return True
        return False
        