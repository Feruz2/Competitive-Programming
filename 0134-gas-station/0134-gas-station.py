class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total = 0
        sur = 0
        start  = 0
        for i in range(len(gas)):
            total += gas[i]
            total -= cost[i]
            sur += gas[i]
            sur -= cost[i]
            if sur < 0:
                sur = 0
                start = i + 1
        return -1 if total < 0 else start
            