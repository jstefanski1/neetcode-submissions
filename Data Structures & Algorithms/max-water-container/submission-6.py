class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,maxA = 0, 0
        r = len(heights) - 1
        

        while l <= r:
            A = min(heights[l], heights[r]) * (r-l)
            maxA = max(maxA, A)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return maxA
