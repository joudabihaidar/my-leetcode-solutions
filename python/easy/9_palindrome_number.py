class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x=str(x)
        reverse=''
        for i in x:
            reverse=i+reverse
        if x==reverse:
            return True
        False