class Solution:
    def simplifyPath(self, path: str) -> str:
        s = []
        string  = path
        sp = path.split('/')
        path =[]
        for val in sp:
            if val != '':
                path.append(val)
       
        for ch in path:
            if ch == '..':
                if s:
                    s.pop()
            elif ch == '.':
                continue
            else:
                s.append('/'+ch)
        return "".join(s) if len(s)>0 else '/'
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         for idx,val in enumerate(path):
#             if val == '':
#                 path[idx] = '/'
#         # print(path)

#         for ch in path:
        
#             if s and s[-1] == ch and ch == '/':
#                 continue
#             elif s and ch == '..':
#                 while len(s) > 1 and s[-1] == '/':
#                     x = s.pop()
#                 if len(s) > 1:
#                     s.pop()
#                 # print(s)
#             else:
#                 s.append(ch)
#                 # print(s)
#         if len(s) > 1 and s[-1] == '/':
#             s.pop()
#         ans = "".join(s)
#         return ans