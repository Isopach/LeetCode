561. Array Partition I

class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)              
        return sum(nums[::2]) #the minimum of each pair in a sorted list will always be the first number 
