class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        
        store = [0] * 10001

        for num in nums:

            if store[num] == 1:
                return num
            store[num] += 1
        