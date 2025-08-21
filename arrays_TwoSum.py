#PROBLEM 2 - ARRAYS
#TWO SUM

class Solution(object):
    def twoSum(self, nums, target):
        
        #dictionary created
        seen={}

        #checking to see if complement exist in dictionary if so, pair is found
        for i,num in enumerate(nums):
            complement=target-num
            if complement in seen:
                return [seen[complement],i]
            seen[num]=i

        
#creating instance and calling and function
sol=Solution()
num=[2,7,11,15]
ret=sol.twoSum(num,9)

#printing output
print(ret)
        