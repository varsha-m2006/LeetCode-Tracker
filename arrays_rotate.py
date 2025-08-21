#PROBLEM 189 - ARRAYS
#ROTATE ARRAY

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        #copy array to store edited version
        new=[]

        #if k lesser than length of nums
        if(k<len(nums)):

            #adding last few elements in the begining
            for i in range(len(nums)-k,(len(nums))):
                new.append(nums[i])

            #rest added after
            for i in range(len(nums)-k):
                new.append(nums[i])
            
            #copying into original array
            for i in range(len(nums)):
                nums[i]=new[i]
            return nums
        #if k is more than length of nums its reminder after division is take as the number of rotations
        else:
            for i in range(len(nums)-k%len(nums),(len(nums))):
                new.append(nums[i])

            for i in range(len(nums)-k%len(nums)):
                new.append(nums[i])

            for i in range(len(nums)):
                nums[i]=new[i]
            return nums

#instance
sol=Solution()
nums=[1,2,3,4,5,6,7]
k=3
ret=sol.rotate(nums,k)

#output
print(ret)
            
        