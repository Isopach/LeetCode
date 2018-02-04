#657. Judge Route Circle

class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        org = (0,0)             #initial pos
        cx = 0; cy = 0          #count of x and y-coord
        cy += moves.count('U')  #adds 1 when up
        cy -= moves.count('D')  #subtracts 1 when down
        cx += moves.count('R')  #adds 1 when right
        cx -= moves.count('L')  #subtracts 1 when left
        if (cx,cy) == org:      #returns True if equal to initial pos
            return True
        else:
            return False
