#PROBLEM 560 - HASHING & ARRAYS
#SUBARRAY SUM EQUALS K

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        #current sum
        cur_sum=0

        #inializing prefix dictionary(prefix sum hashmap)
        prefix={0:1}

        #count of the number of sub arrays
        count=0

        for i in nums:
            #incrementation
            cur_sum+=i

            #is complement exists
            if (cur_sum-k) in prefix:
                count+=prefix[cur_sum-k]

            #if the cur_sum exist increment
            if cur_sum in prefix:
                prefix[cur_sum]+=1
            #initialize to 1 if it doesnt
            else:
                prefix[cur_sum]=1

        return count

#instance
sol=Solution()
nums=[1,1,1]
ret=sol.subarraySum(nums,2)

#outputs
print(ret)


        