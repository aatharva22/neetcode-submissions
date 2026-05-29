class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        if not nums:
            return []
        
        prefix = [0] * (len(nums))
        suffix = [0] * (len(nums))

        prefix[0] = 1
        suffix[len(nums) - 1] = 1

        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] * nums[i-1]
            suffix[len(nums) - i - 1] = suffix[len(nums) - i] * nums[len(nums) - i]
        
        for i in range(len(nums)):
            nums[i] = prefix[i] * suffix[i]
        
        return nums
        