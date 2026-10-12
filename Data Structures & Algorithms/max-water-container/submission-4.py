class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        l, r = 0, len(heights) - 1

        while l < r:
            w = r - l
            h = min(heights[l], heights[r])
            a = w * h
            max_area = max(max_area, a)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return max_area

        
