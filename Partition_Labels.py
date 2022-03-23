class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dicit ={}
        arr = []
    
        for char in s:
            arr.append(char)
        
        for i in range(len(arr)):
            
            dicit[arr[i]] = [i]
      
        final = []
        i = 0
        while i < len(arr):
            end = dicit[arr[i]][0]
            curr = i 
            while curr < end:
                if dicit[arr[curr]][0] > end:
                    end = dicit[arr[j]][0]
                j += 1
            final.append(end - i + 1)
            i = end + 1
        return final