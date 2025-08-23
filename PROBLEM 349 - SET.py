#PROBLEM 349 - SET 
#INTERSECTION OF TWO ARRAYS

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        #two sets for each of the arrays
        set1=set()
        set2=set()

        #adding each of the elements in the arrays inti their respective sets
        for i in nums1:
            set1.add(i)
        for i in nums2:
            set2.add(i)

        #intersection
        return list(set1&set2)

#instance
sol=Solution()
nums1=[1,2,2,1]
nums2=[2,2]
ret=sol.intersection(nums1,nums2)

#output
print(ret)
        