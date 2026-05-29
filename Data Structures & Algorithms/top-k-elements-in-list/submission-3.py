class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = {}

        for num in nums:
            if num in hmap:
                hmap[num] += 1
            else:
                hmap[num] = 1
        
        def return_value(i):
            return hmap[i]
        ans = sorted(hmap, key = return_value, reverse = True)
        return ans[:k]