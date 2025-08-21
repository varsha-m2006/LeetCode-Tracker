#PROBLEM 283 - ARRAYS
#MOVE ZEROES

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        #new array
        new=[]
        #initializing counter for no. of zeroes
        counter=0

        for i in nums:
            #added to new array if not zero
            if i!=0:
                new.append(i)
            #incrementation of counter
            else:
                counter+=1
        
        #adding all zeroes at the end
        for i in range(counter):
            new.append(0)

        #copying into original array
        for i in range(len(nums)):
            nums[i]=new[i]

        return nums

#instance
sol=Solution()
nums=[0,1,0,3,12]
ret=sol.moveZeroes(nums)

#output
print(ret)
        