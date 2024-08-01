class Solution(object):
    def romanToInt(self, roman):
        """
        :type s: str
        :rtype: int
        """
        roman_to_nb={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        integer=""
        for i in roman:
            if i in roman_to_nb:
                integer+="+"+str(roman_to_nb[i])
        integer=integer.split("+")
        integer.remove("")

        s = 0
        i = 0

        while i < len(integer):
            if i + 1 < len(integer) and int(integer[i]) < int(integer[i + 1]):
                s += int(integer[i + 1]) - int(integer[i])
                i += 2 
            else:
                s += int(integer[i])
                i += 1
        return s 
   