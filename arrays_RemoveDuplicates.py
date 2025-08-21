#PROBLEM 26 - ARRAYS
#REMOVE DUPLICATES

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #elements that have already occured once
        seen=set()

        #new array to store edited version
        new=[]
        for i in nums:
            #only unique ones added
            if i not in seen:
                new.append(i)
                seen.add(i)

        #updated num array so that first k elements are all unique 
        for i in range(len(new)):
            nums[i]=new[i]
        
        return len(new)

#instance
sol=Solution()
nums=[1,1,2]
ret=sol.removeDuplicates(nums)

#output
print(ret)


        
        