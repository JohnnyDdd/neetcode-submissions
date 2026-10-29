class Solution:

    def leastInterval(self, tasks: List[str], n: int) -> int:
        dict_t = {}
        for t in tasks:
            dict_t[t] = dict_t.get(t,0) + 1
        heap = [-f for f in dict_t.values()]
        heapq.heapify(heap)

        time = 0
        queue = deque()
        while heap or queue:
            time += 1
            if not heap:
                time = queue[0][1]
            else:
                new_freq = 1 + heapq.heappop(heap)
                if new_freq:  
                    queue.append([new_freq, time + n])
            
            if queue and queue[0][1] == time:
                heapq.heappush(heap, queue.popleft()[0])
        return time
        