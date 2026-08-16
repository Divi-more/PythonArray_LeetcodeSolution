"""**(Sort Array By Parity)**

Solution
Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.
Return any array that satisfies this condition.

Example 1:
Input: nums = [3,1,2,4]
Output: [2,4,3,1]
Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
"""

class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        arr = []
        arr2 = []
        
        for i in nums:
            if i % 2 == 0:
                arr.append(i)
            else:
                arr2.append(i)
                
        res = arr + arr2
        
        return res