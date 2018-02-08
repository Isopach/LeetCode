#292. Nim Game

class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n % 4 != 0   #return true if not divisible by 4, else false
