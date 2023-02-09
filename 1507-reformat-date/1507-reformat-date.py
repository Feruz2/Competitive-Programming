class Solution:
    def reformatDate(self, date: str) -> str:
        dicit = {
            "Jan" : "01",
            "Feb" : "02",
            "Mar" : "03",
            "Apr" : "04",
            "May" : "05",
            "Jun" : "06",
            "Jul" : "07",
            "Aug" : "08",
            "Sep" : "09",
            "Oct" : "10",
            "Nov" : "11",
            "Dec" : "12",
        }
        lst = date.split(" ")
        ans = ""
        ans = lst[2] + "-"
        ans += dicit[lst[1]] + "-"
        num = "0" + lst[0][:-2] if len(lst[0][:-2]) == 1  else lst[0][:-2]
        ans += num
        return ans
        