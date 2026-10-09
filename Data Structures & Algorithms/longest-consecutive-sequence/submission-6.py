class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        num_set = set(nums)
        max_streak = 0

        for number in num_set:
            if number - 1 not in num_set:
                current_number = number
                current_streak = 1

                while current_number + 1 in num_set:
                    current_number += 1
                    current_streak += 1
                max_streak = max(current_streak , max_streak)
    
        return max_streak 