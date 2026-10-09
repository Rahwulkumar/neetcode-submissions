class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        keys = {}

        for number in nums:
            if number not in keys:
                keys[number] = 1
            else:
                keys[number] += 1
                return number
        