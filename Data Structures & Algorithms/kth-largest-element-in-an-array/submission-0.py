class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        #using maxheap 

        for i in range(len(nums)):
            nums[i] = -nums[i]
        maxheap = nums

        heapq.heapify(maxheap)

        for _ in range(k-1):
            heapq.heappop(maxheap)
        return -1 * maxheap[0]
