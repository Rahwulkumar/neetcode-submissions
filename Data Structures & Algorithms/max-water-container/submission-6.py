class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        l, r = 0, n - 1
        result = 0

        while l < r:
            w = r - l
            h = min(heights[l], heights[r])
            area = h * w
            result = max(area, result)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return result
