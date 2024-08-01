class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack=[] 
        for i in range(len(s)):
            if s[i]=="(" or s[i]=="[" or s[i]=="{":
                stack.append(s[i])
            elif not stack:
                return False
            elif s[i]==")" and stack[-1]=="(":
                stack.pop()
            elif s[i]=="]" and stack[-1]=="[":
                stack.pop()
            elif s[i]=="}" and stack[-1]=="{":
                stack.pop()
            else:
                return False
        return len(stack)==0