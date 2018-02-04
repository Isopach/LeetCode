#507. Perfect Number

import math
class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 0:                               #checks if negative
            return False
        divs =[1]                                 #all numbers divisible by 1
        for i in xrange(2,int(math.sqrt(num))+1): #any iterations of i after the sqrt will return False
            if num%i ==0:                         #if divisible, extend the list
                divs.extend([i,num/i])
        divs.extend([num])                        #extend list by divisor
        divs = list(set(divs))                    #convert to list
        divs.remove(num)                          #removes itself
        return sum(divs) == num
