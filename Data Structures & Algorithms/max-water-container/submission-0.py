class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        maxArea = 0
        while l < r:
            hl, hr = heights[l], heights[r]
            area = min(hl, hr) * (r - l)
            maxArea = max(area, maxArea)
            if hl <= hr:
                l += 1
            else:
                r -= 1
        return maxArea
        