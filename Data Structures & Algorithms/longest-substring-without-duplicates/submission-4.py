class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash_map = {}
        left = 0
        max_len = 0

        for right in range(len(s)):
            if s[right] in hash_map and hash_map[s[right]] >= hash_map[s[left]]:
                left = hash_map[s[right]] + 1

            hash_map[s[right]] = right
            max_len = max(max_len, right- left + 1)
        return max_len

        