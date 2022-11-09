class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ans = set()
        def rec(new,idx):
            ans.add(tuple(new)) 
            if idx >= len(s):
                return 
            if not new[idx].isalpha():
                
                rec(list(new),idx+1)
                
            else:
                
                rec(list(new),idx+1)
                if new[idx].isupper():
                    new[idx] = new[idx].lower()
                    rec(list(new),idx+1)
                elif new[idx].islower():
                    new[idx] = new[idx].upper()
                    rec(list(new),idx+1)
            
        rec(list(s),0)
        ans = list(ans)
        new  = []
        for lst in ans:
            lst = list(lst)
            new.append("".join(lst))
        return new