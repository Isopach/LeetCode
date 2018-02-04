#771. Jewels and Stones

class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        total = 0
        for i in xrange(len(J)):
            total += S.count(J[i])
        return total
        
