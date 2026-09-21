class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n in (0,1,2): return 0
        if height[1] > height[0]: return self.trap(height[1:])
        
        i,j = 0,n-1
        max_1 , max_i = 0,0
        max_2 , max_j = 0,0
        while i < j:
            if height[i] > max_1: max_1 , max_i = height[i], i
            if height[j] > max_2: max_2 , max_j = height[j], j
            if max_1 > max_2: j -= 1
            else: i += 1
        if len(set(height[max_i:max_j+1])) == 1: return 0
        vol = 0
        for h in height[max_i+1:max_j]:
            vol += max(0,(min(max_1, max_2) - h))
        return self.trap(height[:max_i+1]) + self.trap(height[max_j:]) + vol