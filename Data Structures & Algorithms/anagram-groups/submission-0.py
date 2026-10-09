class Solution:
    def bubble_sort(self,s):
        str_li = list(s)
        n = len(str_li)
        for i in range(n):
            for j in range(n-i-1):
                if(str_li[j] > str_li[j+1]):
                    str_li[j],str_li[j+1] = str_li[j+1],str_li[j]
        return ''.join(str_li)
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_hash = {}
        for char in strs:
            sorted_word = self.bubble_sort(char)
            if sorted_word not in str_hash:
                str_hash[sorted_word]=[]
            str_hash[sorted_word].append(char)
        return list(str_hash.values())
        