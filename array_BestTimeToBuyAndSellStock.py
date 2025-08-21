#PROBLEM 121 - ARRAYS 
#BEST TIME TO BUY AND SELL STOCK

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        #initializing min and max value
        min=float("inf")
        max=0
        
        #iterating through array, to find maximum profit
        for i in prices:
            if i<min:
                min=i
            elif max<i-min:
                max=i-min
        return max

#creating instance
sol=Solution()
prices=[7,1,5,3,6,4]
ret=sol.maxProfit(prices)

#output
print(ret)