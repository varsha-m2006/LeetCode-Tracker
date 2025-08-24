#PROBLEM 739 - MONOTONIC STACK
#DAILY TEMPERATURES

class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        #length of array
        n = len(temperatures)

        #inializing all as 0
        answer = [0] * n

        #monotonic stack to store index -(always decresing in this case)
        stack = []

        for i, temp in enumerate(temperatures):
            #when you enocunter an element greater than the topmost elemnt index ins stack
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev = stack.pop()
                answer[prev] = i - prev#the no of days
            #adding each of the indices
            stack.append(i)

        return answer

        
        

        