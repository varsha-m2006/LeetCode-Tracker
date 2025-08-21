#PROBLEM 167 - ARRAYS
#TWO SUM II - INPUT ARRAY IS SORTED

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        #similar to problem 2 instead increasing the index number by 1
        seen={}
        for i,num in enumerate(numbers):
            complement=target-num
            if complement in seen:
                return [seen[complement]+1,i+1]
            seen[num]=i

sol=Solution()
nums=[2,7,11,15]
target=6
ret=sol.twoSum(nums,target)
print(ret)
        