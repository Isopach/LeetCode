#771. Jewels and Stones

class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        total = 0                   #initialize total as 0 jewels
        for i in xrange(len(J)):    #loops through length of jewels
            total += S.count(J[i])  #for every jewel present in stones, add 1 to total count
        return total
        
