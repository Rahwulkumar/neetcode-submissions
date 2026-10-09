class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        test_key = {}

        for char in s:
            if char not in test_key:
                test_key[char] = 1
            else:
                test_key[char] += 1
        for char in t:
            if char in test_key:
                test_key[char] -= 1
            else:
                return False
        
        for char in test_key:
            if test_key[char]!= 0:
                return False
        return True
        