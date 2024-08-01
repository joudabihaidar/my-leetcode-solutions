class Solution(object):
    def countSeniors(self, details):
        """
        :type details: List[str]
        :rtype: int
        """
        older_60=0
        for i in range(len(details)):
            if int(details[i][11:13])>60:
                older_60+=1
        return older_60
        