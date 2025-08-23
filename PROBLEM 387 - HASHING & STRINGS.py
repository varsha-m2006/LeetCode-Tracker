#PROBLEM 387 - HASHING & STRINGS
#FIRST UNIQUE CHARCTER IN A STRING

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        #for strong freq of occurences
        hashmap={}

        #counting occurences and storinng for each letters
        for i in range(len(s)):
            if s[i] in hashmap:
                hashmap[s[i]]+=1
            else:
                hashmap[s[i]]=1

        c=0

        #which index has occurance as only 1 us the unique element
        for i in range(len(s)):
            if hashmap[s[i]]==1:
                return i
                c=1
                break

        #when no element is unique
        if c==0:
            return -1

#instance
sol=Solution()
s="leetcode"
ret=sol.firstUniqChar(s)

#output
print(ret)

        