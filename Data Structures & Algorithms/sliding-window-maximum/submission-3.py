class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        ret = []
        pq = []
        for r in range(len(nums)):
            heapq.heappush(pq, (-nums[r], r))
            if r-l+1 >= k:
                while pq[0][1] < l:
                    heapq.heappop(pq)
                l += 1
                val,index = pq[0]
                ret.append(-val)
        return ret