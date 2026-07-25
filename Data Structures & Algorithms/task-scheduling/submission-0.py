class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        counts = Counter(tasks)

        heap = []

        for key, val in counts.items():

            heap.append( -1 * val)
        
        heapq.heapify(heap)

        time = 0

        while heap:

            slot = 0
            temp = []

            while slot < n + 1:

                if heap:
                    count = heapq.heappop(heap)
                    count = count + 1
                    if count < 0:
                        temp.append(count)
                time = time + 1
                slot += 1

                if not heap and not temp:
                    break
                
            for t in temp:
                heapq.heappush(heap,t)
        
        return time
                    














