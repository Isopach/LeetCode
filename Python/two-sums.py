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
                

#Two-pass Hash Table

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ndict = {k: v for v, k in enumerate(nums)}              #Creates a dictionary with element as key and index as value
        r = [0,0]
        for i, num in enumerate(nums):                          #loops through input array
            complement = target - nums[i]                       #initializes complement and defines it as target - current element
            if complement in ndict and ndict[complement] != i:  #if the complement exists and does not equal to current element nums[i]
                r[0] = ndict[complement]                        #sets first element in result to value of complement in ndict i.e. the index
                r[1] = i                                        #sets second element in result to current index 
        return r

    
#One-pass Hash Table
