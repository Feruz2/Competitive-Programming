class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bull = 0
        dicits = defaultdict(int)
        dicitg = defaultdict(int)
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bull += 1
            else:
                dicits[secret[i]] += 1
                dicitg[guess[i]] += 1
        cow = 0
        for key in dicits:
            if key in dicitg:
                cow += min(dicits[key],dicitg[key])
        return str(bull) + "A" + str(cow) + "B"