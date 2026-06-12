class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        store = [0] * 10000

        for i, num in enumerate(nums):
            index = num - 1
            if store[index] == 1:
                return num
            else:
                store[index] += 1
        
