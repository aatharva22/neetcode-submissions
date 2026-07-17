class Solution:
    def climbStairs(self, n: int) -> int:
        
        # Either we can reach n steps by taking 1 step from n-1
        # or 2 steps from n-2
        #so unique ways(n) = unique ways(n-1) + unique ways(n-2)

        if n < 2:
            return n
        prev, curr = 1 , 2

        for _ in range(3,n+1):

            prev,curr = curr, curr+prev
        return curr



