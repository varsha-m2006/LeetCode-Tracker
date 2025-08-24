#PROBLEM 209 - SLIDING POINTER WINDOW
#MINIMUM SIZE SUBARRAY SUM

class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        #left pointer
        i = 0
        #initializing the cur_sum
        curr_sum = 0
        #initializing minimum length
        min_length = float("inf")

        c=0

        #pointer to loop through array
        for j in range(len(nums)):

            #incrementation for each sub array
            curr_sum += nums[j]

            while curr_sum >= target:
                #minumum length
                min_length = min(min_length, j - i + 1)

                #closing the window and moving on to next subarray
                curr_sum -= nums[i]
                c=-1
                i += 1
        if c==-1:
            return min_length
        else:
            return 0

#instance
sol=Solution()
nums=[2,3,1,2,4,3]
ret=sol.minSubArrayLen(7,nums)

#output
print(ret)
        