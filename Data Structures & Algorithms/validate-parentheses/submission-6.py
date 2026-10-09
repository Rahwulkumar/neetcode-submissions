class Solution:
    def isValid(self, s: str) -> bool:
        keys = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }

        stack = []

        for bracket in s:
            if bracket in keys:
                if not stack or stack[-1] != keys[bracket]:
                    return False
                stack.pop()
            else:
                stack.append(bracket)
        return True if not stack else False

