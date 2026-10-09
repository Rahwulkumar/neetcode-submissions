class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hasy = {}
        for i,num in enumerate(nums):
            complement = target-num
            if(complement in hasy):
                return[hasy[complement],i]
            hasy[num] = i
        return []
        