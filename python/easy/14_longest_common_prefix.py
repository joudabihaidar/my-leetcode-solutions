class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        preffix=''
        if not strs:  
            return preffix
        for letter in range(len(strs[0])):
            current_letter=strs[0][letter]
            for word in range(len(strs)):
                if letter>=len(strs[word]):
                    return preffix
                if strs[word][letter]!=current_letter:
                    return preffix
            preffix+=current_letter
        return preffix