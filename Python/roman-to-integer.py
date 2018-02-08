#13. Roman to Integer
#ans += s.count('I')*1 + s.count('V')*5 + s.count('X')*10 + s.count('X')*10 + s.count('L')*50 + s.count('C')*100 + s.count('D')*500 + s.count('M')*1000 
#this doesn't work as XI = IX which isn't correct

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        r = {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
        for i in range(0,len(s)-1):
            if r[s[i]] < r[s[i+1]]: #if current is less than next then - current (eg. IX is 10-1 instead of XI is 10+1)
                ans -= r[s[i]]
                
            else:
                ans += r[s[i]]      #else just add it 
            
        return ans + r[s[-1]]       #return answer plus last character in s
