class Solution:
    def isPalindrome(self, s: str) -> bool:
        updated_string = "".join(char.lower() for char in s if char.isalnum())

        lft = 0
        right = len(updated_string)-1

        while lft < right:
            if updated_string[lft] != updated_string[right]:
                return False
            right -= 1
            lft += 1
        return True
        