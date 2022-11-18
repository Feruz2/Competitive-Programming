class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        ans  = [0]*(n+2)
        for i in range(len(bookings)):
            ans[bookings[i][0]] += bookings[i][2]
            ans[(bookings[i][1])+1] += -1*bookings[i][2]
        cur = 0
        # print(ans)
        for i in range(len(ans)):
            cur += ans[i]
            ans[i] = cur
        ans.pop()
        return ans[1:]