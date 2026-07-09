class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water = 0
        l,r = 0, len(heights)-1
        while l<r:
            if heights[l]<heights[r]:
                max_water = max(max_water, heights[l]*(r-l))
                l+=1
            else:
                max_water = max(max_water, heights[r]*(r-l))
                r-=1
        return max_water
        