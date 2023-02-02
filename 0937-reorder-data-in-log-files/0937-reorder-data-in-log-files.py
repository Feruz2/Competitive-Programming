class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digit = []
        letter = []
        for i in range(len(logs)):
            x = logs[i].split()
            if x[1].isalpha():
                letter.append(x)
            else:
                digit.append(logs[i])
                
        
        letter.sort(key = lambda x : (x[1:],x[0]))
        
    
        
        final = []
        
        for i in range(len(letter)):
            new = " ".join(letter[i])
            final.append(new)

        return final + digit