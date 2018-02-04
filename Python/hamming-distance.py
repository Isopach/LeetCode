class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        x = bin(x)[2:].zfill(100)
        y = bin(y)[2:].zfill(100)
        #super hacky way to getting past length mistmatch assertion
        assert len(x) == len(y), "Houston, we've got a problem!" #checks if length of x == length of y
        return sum(c1 != c2 for c1, c2 in zip(x, y))             #sums a list of indexes where x is different from y
