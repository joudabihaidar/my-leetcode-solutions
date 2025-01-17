class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle not in haystack:
            return -1
        else:
            i=0
            a=haystack[i:len(needle)]
            if a!=needle:
                while a != needle:         
                    i+=1
                    a=haystack[i:len(needle)+i]
            return i