class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_list = {}
        for char in s:
            if char in char_list:
                char_list[char] +=1
            else:
                char_list[char] =1
        for char in t:
            if char in char_list:
                char_list[char] -= 1
            else:
                return False
        for i in char_list:
            if(char_list[i]!= 0):
                return False
        return True       