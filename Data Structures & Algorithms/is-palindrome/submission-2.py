class Solution:
    def isPalindrome(self, s: str) -> bool:
        updated_string = "".join(char.lower() for char in s if char.isalnum())

        left = 0
        right = len(updated_string)-1

        while left < right:
            if updated_string[left] != updated_string[right]:
                return False
            
            left += 1
            right -= 1
        return True
        