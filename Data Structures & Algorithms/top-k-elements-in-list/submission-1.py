class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = {}

        for num in nums:
            if num in hmap:
                hmap[num] +=1
            else :
                hmap [num] = 1
        
        sorted_list = sorted(hmap.items(), key = lambda x:x[1] , reverse = True)
        return [num for num, _ in sorted_list[:k]]