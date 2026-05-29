class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        
        longest = 1
        current = 1

        nums = sorted(set(nums))

        for i in range(1, len(nums)):
            
            if nums[i-1] + 1 == nums[i]:
                current += 1
                
            else:
                current = 1
            longest = max(current,longest)
            
        

        return longest