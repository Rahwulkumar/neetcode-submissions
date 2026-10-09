class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        keys = {}
        for i in nums:
            if i not in keys:
                keys[i] = 1
            else:
                keys[i] += 1
        for num in keys:
            if keys[num] > 1:
                return True
        return False
        


        