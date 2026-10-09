class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_list = []
        max_len = 0
        left = 0

        for right in range(k, len(nums)+1):
            sample_list = nums[left :right]
            max_list.append(max(sample_list))
            left+=1
        return max_list

