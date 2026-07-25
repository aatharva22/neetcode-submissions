class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        #by max heap approach

        maxHeap = []

        for x,y in points:

            dist = -1 * (x*x + y*y)
            maxHeap.append((dist,x,y))
        
        heapq.heapify(maxHeap) #TC O(n)

        while len(maxHeap) > k:

            heapq.heappop(maxHeap)
        res = []
        while maxHeap:

            dist, x, y = heapq.heappop(maxHeap)
            res.append([x,y])
        return res
