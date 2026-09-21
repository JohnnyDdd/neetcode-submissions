class Solution:
    def maxArea(self, heights: List[int]) -> int:
        height_candidates = set()
        n = len(heights)
        i,j = 0, n-1
        max_h = 0
        while i < j:
            hi = heights[i]
            hj = heights[j]
            if max_h < min(hi,hj) * (j-i):
                max_h = min(hi,hj) * (j-i)
            if hi <= hj: i+=1
            else: j-=1
        return max_h