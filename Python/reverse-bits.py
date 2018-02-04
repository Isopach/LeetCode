#190. Reverse Bits

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        n = '{0:032b}'.format(n)
        n = n[::-1]
        return int(n,2)
