#557. Reverse Words in a String III

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s=s.split()               #split string into list on whitespace
        xs = [x[::-1] for x in s] #reverse each element in list       
        return ' '.join(xs)       #join each element of list to string
