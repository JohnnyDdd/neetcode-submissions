class Solution:

    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = []
        dict_t = {}
        for t in tasks:
            dict_t[t] = dict_t.get(t,0) + 1
        for t in dict_t.keys():
            heapq.heappush(heap,(-dict_t[t],t))

        time = 0
        queue = deque()

        while heap or queue:
            time += 1
            #print(time)
            if heap:
                #print("available task exists")
                nf, cur_task = heapq.heappop(heap)
                if nf + 1 < 0:  
                    queue.append((nf + 1, cur_task, time + n))
            if queue:
                #check availability
                nf, closest_task, at = queue[0]
                if time >= at: 
                    queue.popleft()
                    heapq.heappush(heap,(nf, closest_task))
        return time
        