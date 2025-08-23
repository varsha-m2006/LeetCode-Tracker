#PROBLEM 290 - HASHING & ARRAYS
#WORD PATTERN

class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        #creating hashmaps for both pattern and string giving them each a consecutive number starting from 0
        hashmap1={}
        c=0
        for i in list(pattern):
            if i not in hashmap1:
                hashmap1[i]=c
                c+=1
                
        
        hashmap2={}
        c2=0
        for i in list(s.split(" ")):
            if i not in hashmap2:
                hashmap2[i]=c2
                c2+=1
        #making them intio two list in terms if the numbers in the hashmap
        l1=[]
        l2=[]

        for i in list(s.split(" ")):
            l1.append(hashmap2[i])

        for i in list(pattern):
            l2.append(hashmap1[i])

        p=0
        #if length is equal
        if(len(l1)==len(l2)):
            #checking if it follows the pattern
            for i in range(len(l1)):
                if l1[i]!=l2[i]:
                    p=-1
                    return False
            if p==0:
                return True
        else:
            return False

#instance
sol=Solution()
p="abba"
s="dog cat cat dog"
ret=sol.wordPattern(p,s)

#output
print(ret)
                

            
            
        