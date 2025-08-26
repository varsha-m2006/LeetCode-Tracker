#PROBLEM 69 - BINARY SEARCH
#SQRT(X)

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        left=0
        right=x

        #binary serach applied here to find the root if its a perfecr square
        while left<=right:
            m=(left+right)//2
            if round(m*m)==x:
                return m
            elif round(m*m)<x:
                left=m+1
            else:
                right=m-1
                
        #if not a perfect square nearest integer returned(through examples find out weather its left or right)
        return right

        