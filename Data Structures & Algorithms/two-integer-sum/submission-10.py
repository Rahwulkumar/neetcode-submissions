class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i, num in enumerate(nums):
            ans = target - num
            if ans in hash_map:
                return[hash_map[ans], i]
            hash_map[num] = i
        return
        