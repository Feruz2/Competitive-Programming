class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        num=0
        list=[0]*60

        for i in time:
            k = i%60

            if(k==0):
                num+=list[k]
            else:
                num+=list[60-k]
            
            list[k]+=1
        return num
        