class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        ans = 0
        curr = gas[0]
        for i in range(1,len(gas)):
            if curr < cost[i-1]:
                ans = i
                curr = gas[i]
            else:
                curr -= cost[i-1]
                curr += gas[i]
        
        curr = gas[ans]
        for i in range(ans + 1,ans + 1 + len(gas)):
            if curr < cost[(i-1)%len(gas)]:
                return -1
                
            else:
                curr -= cost[(i-1)%len(gas)]
                curr += gas[i%len(gas)]
        return ans