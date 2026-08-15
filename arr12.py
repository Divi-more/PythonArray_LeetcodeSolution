"""**(Move Zeroes)**
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.

Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
"""

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        arr1 = []
        arr2 = []
        
        for i in nums:
            if i != 0:
                arr1.append(i)
            else:
                arr2. append(i)
        
        res = arr1 + arr2
        print(res)    