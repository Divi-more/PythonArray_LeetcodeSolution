""" **(Duplicate Zeros)**
Given a fixed-length integer array arr, duplicate each occurrence of zero, 
shifting the remaining elements to the right.
Note that elements beyond the length of the original array are not written. 
Do the above modifications to the input array in place and do not return anything.

Example 1:
Input: arr = [1,0,2,3,0,4,5,0]
Output: [1,0,0,2,3,0,0,4]
Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]
"""

class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        i = 0
        
        while i < len(arr):
            if arr[i] == 0:
                arr.insert(i + 1, 0) #insert 0 at i+1 location
                arr.pop()          # Keep the length the same
                i += 1             # Skip the duplicated zero
            i += 1