class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        new = []
        for i in range(len(plantTime)):
            new.append((growTime[i],plantTime[i]))
        new.sort(key = lambda x : -x[0])
        ans = 0
        soFar = 0
        for grow, plant  in new:
            
            ans = max(ans,soFar+plant+grow)
            soFar += plant
        return ans