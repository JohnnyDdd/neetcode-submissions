class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.length = k
        for num in nums:
            self.add(num)
        heapq.heapify(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.length:
            heapq.heappop(self.heap)
        return self.heap[0]

