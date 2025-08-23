#PROBLEM 3 - SET & SLIDING POINTER
#LONGEST SUBSTRING WITHOUT REPEATING CHARACTERS

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        #elements that have already been encountered
        seen = set()
        #left pointer
        j=0
        #max length initialized to zero
        max_length=0

        #right pinter to iterate through current letters
        for i in range(len(s)):
            #sliding pointer
            while s[i] in seen:
                seen.remove(s[j])
                j+=1                            #closing the window
            seen.add(s[i])
            max_length=max(max_length,i-j+1)    #max length updated
        
        return max_length

#instance
sol=Solution()
s="abcabcbb"
ret=sol.lengthOfLongestSubstring(s)

#output
print(ret)


        
        