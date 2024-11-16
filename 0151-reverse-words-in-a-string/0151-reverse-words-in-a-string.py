class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        lst = s.split()

        for i in range(len(lst) // 2):
            lst[i], lst[len(lst) - 1 - i] = lst[len(lst) - 1 - i], lst[i]
        
        return " ".join(lst)