#PROBLEM 49 - HASHING & ARRAYS
#GROUP ANAGRAMS

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        #creating hashmap to store words with the same set of letters in key value pairs
        hashmap=defaultdict(list)

        for i in strs:
            #letters of each element
            letters=[]
            #adding all the letters
            for k in range(len(i)):
                letters.append(i[k])
            #make it into a tuple
            t_letters=tuple(sorted(letters))
            #appending
            if t_letters in hashmap:
                    hashmap[t_letters].append(i)
            else:
                hashmap[t_letters].append(i)

        #returnung the values
        return hashmap.values()

#instance
sol=Solution()
strs=["eat","tea","tan","ate","nat","bat"]
ret=sol.groupAnagrams(strs)

#output
print(ret)
