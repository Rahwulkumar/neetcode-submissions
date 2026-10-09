class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        left = 0
        hash_set = {}

        for right in range(len(s)):
            if s[right] in hash_set and hash_set[s[right]] >= left:
                left = hash_set[s[right]] + 1
            hash_set[s[right]] = right
            max_len = max(max_len, right - left + 1)
        return max_len

        