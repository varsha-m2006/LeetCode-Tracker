#PROBLEM 347 - HASHING AND ARRAYS
#TOP K FREQUENT ELEMENENTS

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        #frequency of occurences stored here
        freq={}
        for i in nums:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1

        s=[]

        #appending to s such that values precede keys
        for num,v in freq.items():
            s.append((v,num))

        #sorting from highest to least
        s_sorted=sorted(s,reverse=True)

        new =[]

        #accesing first k elements
        for i in range(k):
            new.append(s_sorted[i][1])
        
        return new
        
#instance
sol=Solution()
nums=[1,1,1,2,2,3]
ret=sol.topKFrequent(nums,2)

#output
print(ret)


        