""" **(Find Numbers with Even Number of Digits)**
Given an array nums of integers, return how many of them contain an even number of digits.
Example 1:
Input: nums = [12,345,2,6,7896]
Output: 2
Explanation: 
12 contains 2 digits (even number of digits). 
345 contains 3 digits (odd number of digits). 
2 contains 1 digit (odd number of digits). 
6 contains 1 digit (odd number of digits). 
7896 contains 4 digits (even number of digits). 
Therefore only 12 and 7896 contain an even number of digits.
"""

class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        
        for num in nums:
            if len(str(num)) % 2 == 0:
                count += 1
        return count
                       
            
"""
To check the length of a number in Python, the most common and Pythonic method is to convert the 
number to a string and use the len() function

For Integers
Use len(str(abs(num))) to handle negative numbers correctly by ignoring the minus sign.
"""