class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        
        if n == 2:
            return max(nums[0], nums[1])

        #Exclude last
        prev1 = nums[0]
        curr1 = max(nums[0], nums[1])

        for i in range(2,n-1):

            prev1,curr1 = curr1, max(curr1, prev1 + nums[i])

        #Exclude 1st
        prev2 = nums[1]
        curr2 = max(nums[1], nums[2])

        for i in range(3,n):

            prev2,curr2 = curr2, max(curr2, prev2 + nums[i])
        
        return max(curr1,curr2)
        