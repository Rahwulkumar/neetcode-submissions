class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        key_s = {}

        for i in s:
            if i in key_s:
                key_s[i] += 1
            else:
                key_s[i] = 1
            
        for j in t:
            if j in key_s:
                key_s[j] -= 1
            else:
                return False

        for char in key_s:
            if key_s[char]!= 0:
                return False
        return True      