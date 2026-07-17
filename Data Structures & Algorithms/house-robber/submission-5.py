class Solution:
    def rob(self, nums: List[int]) -> int:
        
        
        n = len(nums)
        if n == 1:
            return nums[0]
        dp = [None] * (n)

        dp[0] = nums[0]
        dp[1] = max(dp[0], nums[1])

        def bestTillNow(i):
            if i<0:
                return 0
                
            if dp[i] is not None:
                return dp[i]
            
            dp[i] = max(bestTillNow(i-1), nums[i] + bestTillNow(i-2)) 
            return dp[i]

        return bestTillNow(n-1)