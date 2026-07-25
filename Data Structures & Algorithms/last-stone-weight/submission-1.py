class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        for i in range(len(stones)):
            stones[i] = -1 * stones[i]
        
        maxHeap = stones
        heapq.heapify(maxHeap)
        w1 = 0
        w2 = 0
        while maxHeap:
            w1 = -1 * heapq.heappop(maxHeap)
            if maxHeap:
                w2 = -1 * heapq.heappop(maxHeap)
            else:
                return w1
            
            heapq.heappush(maxHeap, -1 * (w1-w2) )
        return w1 

        

        