class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        numSet = set(nums)
        longest = 0

        for num in nums:

            if num - 1 not in numSet:

                curr = 0
                while curr + num in numSet:
                    curr += 1
                longest = max(curr,longest)
        
        return longest