class Solution:

    def numberToWords(self, num: int) -> str:
        if(num == 0):
            return "Zero"

        dictionary = {
            1 : ["One", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"],
            2 : ["Two", "Twenty"],
            3 : ["Three", "Thirty"],
            4 : ["Four", "Forty"],
            5 : ["Five", "Fifty"],
            6 : ["Six", "Sixty"],
            7 : ["Seven", "Seventy"],
            8 : ["Eight", "Eighty"],
            9 : ["Nine", "Ninety"]
        }
        l = ["Thousand", "Million", "Billion"]
        res = []
        i = -1
        while(num > 0):
            a = num % 10
            num //= 10
            b = num % 10
            num //= 10
            c = num % 10
            num //= 10
            if(a == b == c == 0):
                pass
            elif(b == 1):
                if(i != -1): res.append(l[i])
                res.append(dictionary[b][a + 1])
            else:
                if(i != -1): res.append(l[i])
                if(a != 0): res.append(dictionary[a][0])
                if(b != 0): res.append(dictionary[b][1])
            if(c == 0):
                pass
            else:
                res.append("Hundred")
                res.append(dictionary[c][0])
            i += 1
        return " ".join(res[::-1])