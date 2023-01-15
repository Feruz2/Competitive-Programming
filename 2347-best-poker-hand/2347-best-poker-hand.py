class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        dicit = defaultdict(list)
        for i in range(len(ranks)):
            dicit[ranks[i]].append(suits[i])
        if len(set(suits)) == 1:
            return "Flush"
        maximum = 0
        for key in dicit:
            maximum = max(len(dicit[key]),maximum)
        if maximum >= 3:
            return "Three of a Kind"
        if maximum == 2:
            return "Pair"
        else:
            return "High Card"