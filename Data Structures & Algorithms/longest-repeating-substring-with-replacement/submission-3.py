class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left = 0
        result = 0
        frequency = 0

        for right in range(len(s)):
            if s[right] not in count:
                count[s[right]] = 0
            count[s[right]] += 1

            if frequency < count[s[right]]:
                frequency = count[s[right]]
            
            while (right-left+1) - frequency > k:
                count[s[left]] -= 1
                left += 1
            
            result = max(right-left+1, frequency)
        return result


        