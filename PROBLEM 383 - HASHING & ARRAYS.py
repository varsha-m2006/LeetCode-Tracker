#PROBLEM 383 - HASHING & ARRAYS
#RANSOM NOTES

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        #creating hashmaps for both the magazine and ransome notes for the occurances of each of the letters
        hashmap1={}
        m=list(magazine)

        for i in m:
            if i not in hashmap1.keys():
                hashmap1[i]=1
            else:
                hashmap1[i]+=1
        
        r=list(ransomNote)
        hashmap2={}

        for i in r:
            if i not in hashmap2.keys():
                hashmap2[i]=1
            else:
                hashmap2[i]+=1

        #counter
        c=0

        #checking if occurance is same for all the letters in ransom note
        for key in hashmap2.keys():
            if key in hashmap1.keys() and hashmap1[key]>=hashmap2[key]:
                c+=1 #incrementation
                
        #if all letters are there return TRUE
        if c==len(hashmap2.keys()):
            return True
        else:
            return False

#instance
sol=Solution()
ret=sol.canConstruct("a","b")

#output
print(ret)



        