class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        keys = {}
        for index, number in enumerate(nums):
            complement = target - number

            if complement in keys:
                return [keys[complement], index]
            keys[number] = index


