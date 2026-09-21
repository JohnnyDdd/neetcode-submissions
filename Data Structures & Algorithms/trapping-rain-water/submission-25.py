class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 0: return 0
        pre_max = [0] * n
        suf_max = [0] * n
        
        pre_max[0] = height[0]
        for i in range(1,n):
            pre_max[i] = max(pre_max[i-1], height[i])

        suf_max[n-1] = height[n-1]
        for i in range(n-2,-1,-1):
            suf_max[i] = max(suf_max[i+1], height[i])

        val = 0
        for i in range(n):
            val += max(min(suf_max[i],pre_max[i])-height[i], 0)
        return val