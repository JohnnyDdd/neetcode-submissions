class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap,ret = [], []
        p_dict = {}
        for p in points:
            x, y = p[0], p[1]
            dist_sqr = x**2 + y**2
            if dist_sqr not in p_dict.keys(): 
                p_dict[dist_sqr] = [p]
            else: p_dict[dist_sqr].append(p)
            heapq.heappush (heap, (-dist_sqr,p))
            if len(heap) > k:
                heapq.heappop(heap)
        return [tup[1] for tup in heap]