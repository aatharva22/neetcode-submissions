class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        nums = sorted(set(nums))
        largest = 1
        current = 1

        for i in range(1,len(nums)):

            if nums[i] - 1 == nums[i-1]:
                current += 1
                largest = max(current,largest)

            else:
                current = 1
        
        return largest
                    