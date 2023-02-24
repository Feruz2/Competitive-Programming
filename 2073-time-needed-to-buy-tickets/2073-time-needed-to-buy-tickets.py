class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time=0
        at_k=tickets[k]
        count=0
        for i in range(len(tickets)):
            if i>k and tickets[i] >= at_k:
                count+=1
            time=time+min(tickets[i],at_k)
        return time-count