class Solution:
    def isPalindrome(self, s: str) -> bool:
        updated_string = "".join(char.lower() for char in s if char.isalnum())

        low = 0
        right = len(updated_string)-1

        while low < right:
            if updated_string[low] != updated_string[right]:
                return False
            low += 1
            right -= 1
        return True    