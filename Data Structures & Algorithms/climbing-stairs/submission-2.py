class Solution:
    def climbStairs(self, n: int) -> int:
        
        # Either we can reach n steps by taking 1 step from n-1
        # or 2 steps from n-2
        #so unique ways(n) = unique ways(n-1) + unique ways(n-2)

        memo = {1:1, 2:2}

        def fibo(x):

            if x in memo:
                return memo[x]
            else:
                memo[x-1] = fibo(x-1)
                memo[x] = memo[x-1] + memo[x-2]
                return memo[x]
        
        return fibo(n)

        

