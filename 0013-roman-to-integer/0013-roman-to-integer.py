class Solution(object):
    def romanToInt(self, str):
        """
        :type s: str
        :rtype: int
        """
        values = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
        }

        str = str[::-1]
        old = 0
        sum = 0

        for x in str:
            new = values[x]

            if new >= old:
                sum += new
            else:
                sum -= new

            old = new

        return sum