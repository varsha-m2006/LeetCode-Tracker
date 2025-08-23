#PROBLEM 242 - HASHING & ARRAYS
#VALID ANAGRAM

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        #creating hashmap to store sorted list of letters 
        hashmap=defaultdict(list)

        #tuple 
        letters=tuple(sorted(list(s)))

        #add as a key value pair
        hashmap[letters]+=s

        #letters of t string
        letters_t=tuple(sorted(list(t)))
        
        #check if its the same
        if letters_t in hashmap.keys():
            return True
        else:
            return False

#instance
sol=Solution()
s="anagram"
t="nagaram"
ret=sol.isAnagram(s,t)

#output
print(ret)
        


        