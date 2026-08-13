"""**(Check If N and Its Double Exist)**

Solution
Given an array arr of integers, check if there exist two indices i and j such that :
i != j
0 <= i, j < arr.length
arr[i] == 2 * arr[j]
 

Example 1:
Input: arr = [10,2,5,3]
Output: true
Explanation: For i = 0 and j = 2, arr[i] == 10 == 2 * 5 == 2 * arr[j]
"""

class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        
        seen = set()
        
        for i in arr:
            if i * 2 in seen:
                return True
            
            if i % 2 == 0 and i // 2 in seen:
                return True
            
            seen.add(i)
            
        return False
        
        
# arr = (10,2,5,3)