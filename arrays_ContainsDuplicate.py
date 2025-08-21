#PROBLEM 217 - ARRAYS
#CONTAINS DUPLICATE

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        #to store items that has had atleast one occurance in the array
        seen=set()
        for i in nums:
            #if duplicate exists
            if i in seen:
                return True
            #if it doesn't, added to seen set
            else:
                seen.add(i)
        
        return False

#instance
sol=Solution()
nums=[1,2,3,1]
ret=sol.containsDuplicate(nums)

#output
print(ret)
    
        