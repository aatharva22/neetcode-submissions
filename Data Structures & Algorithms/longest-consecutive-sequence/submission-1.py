class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if len(nums) == 0:
            return 0

        nums = sorted(set(nums))

        largest = 1
        current = 1

        for i in range(1,len(nums)):
            if nums[i-1] + 1 == nums[i]:
                current += 1
                largest = max(largest,current)
            else :
                current = 1
        
        return largest