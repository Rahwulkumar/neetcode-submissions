class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_hash= {}
        for char in s:
            if char not in s_hash:
                s_hash[char] = 1
            else:
                s_hash[char] += 1

        for char in t:
            if char in s_hash:
                s_hash[char] -= 1
            else:
                return False
        for char in s_hash:
            if s_hash[char] != 0:
                return False
        return True
            