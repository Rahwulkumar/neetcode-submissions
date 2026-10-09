class Solution:
    def isValid(self, s: str) -> bool:
        key_map = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }
        
        stak = []

        for bracket in s:
            if bracket not in key_map:
                stak.append(bracket)
            else:
                if not stak:
                    return False
                else:
                    popped  = stak.pop()
                    if popped != key_map[bracket]:
                        return False
        return not stak