class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = []
        for num in nums:
            has_duplicates = False
            for seen_num in seen:
                if(seen_num == num):
                    has_duplicates = True
                    break
            if has_duplicates:
                return True
            
            seen.append(num)
        return False
            
         