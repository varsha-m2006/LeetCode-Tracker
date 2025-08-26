#PROBLEM 278 - BINARY SEARCH
#FIRST BAD VERSION

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """

        left=1
        right=n

        #binary searcg
        while left<right:

            #middle element
            m=(left+right)//2

            #if bad version found, we need to check if there is a previous bad verison so we bove to the left partition
            if isBadVersion(m):
                right=m
            #othervise right partition
            else:
                left=m+1

        #the position of the frist bad version
        return left
        