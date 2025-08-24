#PROBLEM 703 - MONOTONIC STACK
#NEXT GREATER ELEMENT II

class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #length of array
        n=len(nums)

        #monotonic stack thats continously decreasing
        output=[]

        #initialzing all as -1
        result=[-1]*n

        #traverse twice to activate circular nature
        for i in range(2*len(nums)):
            #for when traversing twice
            num=nums[i%n]

            #similary here using the monotonic stack method
            while output and nums[output[-1]]<num:
                p=output.pop()
                result[p]=num
                
            #appending the indices of the elements
            if i<n:
                output.append(i)
            
        return result


                




        