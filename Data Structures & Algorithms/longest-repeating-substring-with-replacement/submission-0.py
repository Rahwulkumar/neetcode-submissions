class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left = 0
        max_frequency = 0
        result = 0

        for right in range(len(s)):
            char = s[right]

            if char not in count:
                count[char] = 0
            count[char] += 1

            if count[char] > max_frequency:
                max_frequency = count[char]

            while (right-left+1) - max_frequency > k:
                left_char = s[left]
                count[left_char] -= 1
                left +=1 
            
            result = max(result, right - left + 1)
        return result




        
        


                


        