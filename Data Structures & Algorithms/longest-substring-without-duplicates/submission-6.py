class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        max_len = 0
        key_pair = {}

        for right in range(len(s)):
            if s[right] in key_pair and key_pair[s[right]] >= key_pair[s[left]]:
                left = key_pair[s[right]] + 1
            
            key_pair[s[right]] = right
            max_len = max(max_len, right - left + 1)
        
        return max_len 


        