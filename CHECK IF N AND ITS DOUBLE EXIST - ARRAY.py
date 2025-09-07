#CHECK IF N AND ITS DOUBLE EXIST - ARRAYS AND SET
#PROBLEM 1346

class Solution(object):
    def checkIfExist(self, arr):
        #set of seen items
        seen = set()
        #iterating through all the elements
        for num in arr:
            #checking if double/half exists
            if 2 * num in seen or (num % 2 == 0 and num // 2 in seen):
                return True
            #adding if not
            seen.add(num)
        #if double not found
        return False
