class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hmap = {}

        for i in range(len(nums)):
            if nums[i] in hmap:
                hmap[nums[i]] += 1
            else:
                hmap[nums[i]] = 1
        
        ans = [key for key,val in sorted(hmap.items(), key = lambda items:items[1], reverse = True)[:k]]
        return ans