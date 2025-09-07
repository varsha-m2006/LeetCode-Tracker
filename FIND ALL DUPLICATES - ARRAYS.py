#FIND ALL DUPLICATES - ARRAYS
#PROBLEM 442

class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        seen=set()
        r=[]
        for i in nums:
            if i in seen:
                r.append(i)
            else:
                seen.add(i)
        return r