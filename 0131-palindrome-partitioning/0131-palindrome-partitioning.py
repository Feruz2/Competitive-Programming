class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        ans = []
        def is_palindrom(i, j, s):
            
            left = i
            right = j
            while left <= right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True
        
        def rec(lst, idx, s):
            print(lst, idx)
            if idx >= len(s):
               
                ans.append(lst[:])
                
                return
            
            for i in range(idx, len(s)):
                
                if is_palindrom(idx, i, s):
                    
                    rec(lst + [s[idx: i+1]] ,i + 1, s )
                    
                   
                    
  
        rec([], 0, s)
        return ans
        
        