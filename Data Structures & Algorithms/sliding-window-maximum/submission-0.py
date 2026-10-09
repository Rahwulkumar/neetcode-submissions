class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_window = nums[:k]
        max_list = []
        left = 0
        
        for right in range(k ,len(nums)+1):
            max_window = nums[left: right]
            max_list.append(max(max_window))
            left += 1
        return max_list