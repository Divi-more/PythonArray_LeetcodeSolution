"""**(Squares of a Sorted Array)**
Solution
Given an integer array nums sorted in non-decreasing order, 
return an array of the squares of each number sorted in non-decreasing order.

Example 1:
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
"""

class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        res = []
        
        for num in nums:
            res.append(num ** 2)
            
        res.sort()
        return res
    
"""
arr = [5,3,7,1,-8]

res = []

for num in arr:
    res.append(num ** 2)
    
res.sort()
print(res)

"""