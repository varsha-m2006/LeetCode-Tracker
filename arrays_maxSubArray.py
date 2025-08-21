#PROBLEM 53 - ARRAYS
#MAXIMUM SUBARRAY

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        #inializing
        max_sum=nums[0]
        current_sum=nums[0]

        #finding max sum
        for i in nums[1:]:
            current_sum=max(i,current_sum+i)
            max_sum=max(max_sum,current_sum)
        
        return max_sum

#instance
sol=Solution()
nums=[-2,1,-3,4,-1,2,1,-5,4]
ret=sol.maxSubArray(nums)

#output
print(ret)
            
        
        