#PROBLEM 11 - TWO POINTER
#CONTAINER WITH MOST WATER

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        #left pointer
        i=0

        #right pointer
        j=len(height)-1
        
        #inializing maximum area as 0
        max_area=0
        
        #while left<right
        while i<j:
            #updating current area
            cur_area=min(height[i],height[j])*(j-i) 

            #updating maximum area
            max_area=max(max_area,cur_area)

            #moving left pointer forwards
            if height[i]<height[j]:
                i+=1
            
            #moving right backwards
            else:
                j-=1

        return max_area

#instance
sol=Solution()
h=[1,8,6,2,5,4,8,3,7]
ret=sol.maxArea(h)

#output
print(ret)



        