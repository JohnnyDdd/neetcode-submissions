class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap=[]
        for p in points:
            x, y = p[0], p[1]
            dist_sqr = x**2 + y**2
            heapq.heappush (heap, (-dist_sqr,p))
            if len(heap) > k:
                heapq.heappop(heap)
        return [tup[1] for tup in heap]