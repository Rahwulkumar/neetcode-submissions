class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        key_pair = {}
        for ch in s:
            if ch not in key_pair:
                key_pair[ch] = 1
            else:
                key_pair[ch] += 1
        for ch in t:
            if ch in key_pair:
                key_pair[ch] -= 1
            else:
                return False
        
        for num in key_pair:
            if key_pair[num] != 0:
                return False
        return True
        