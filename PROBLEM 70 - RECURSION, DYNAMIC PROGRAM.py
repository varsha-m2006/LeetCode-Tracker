#PROBLEM 70 - RECURSION, DYNAMIC PROGRAMMING
#CLIMBING STAIRS

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        #if its 1 or 2 steps its the same number ways to reach there 
        if n<=2:
            return n

        #initializing 0 for all steps
        dp=[0]*(n+1)
        dp[1],dp[2]=1,2

        #recursion thprugh dynamic programming
        for i in range(3,n+1):
            dp[i]=dp[i-1]+dp[i-2]
            
        #number of ways to reach n steps
        return dp[n]

        
        