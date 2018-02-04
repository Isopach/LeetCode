#728. Self Dividing Numbers

class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        def isSelfDividing(number):
            for s in str(number):
                if s == '0' or number % int(s) > 0: #checks if it contains 0 or cannot be divided (w/0 remainder) by any character in its string
                    return False
            return True
            
        ans=[]
        for number in range(left,right+1): #loops through range of numbers from left to right bound
            if isSelfDividing(number):
                ans.append(number)         #appends answer to list
                
        return ans                         #returns list
