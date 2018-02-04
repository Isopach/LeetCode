#1. Two Sums

#Brute Force Approach O(n^2)
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        search = {}
        for i, num in enumerate(nums):          #loops through array O(n^2)
            if target - num in search:          #get element num (nums[i]) and find if theres another value that == target - num
                return search[target-num], i
            else:
                search[num] = i                 #repeat search for next element
                

#
