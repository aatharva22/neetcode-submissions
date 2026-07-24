class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        seen = {}

        for num in nums:
            if num in seen:
                seen[num] += 1
            else:
                seen[num] = 1
        
        ans = [key for key,value in sorted(seen.items(), key = lambda x:x[1], reverse = True)[:k] ]
        return ans