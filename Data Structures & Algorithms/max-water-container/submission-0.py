class Solution:
    def maxArea(self, heights: List[int]) -> int:
        largest = 0
        n = len(heights)
        r,l = 0, n-1

        while r < l:
            area = min(heights[r], heights[l]) * (l-r)
            largest = max(area, largest)
            if heights[r] == heights[l]:
                r += 1
                l -= 1
            elif heights[r] > heights[l]:
                l -= 1
            elif heights[r] < heights[l]:
                r += 1
        
        return largest