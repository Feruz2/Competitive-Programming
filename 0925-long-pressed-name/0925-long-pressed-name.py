class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        j = 0
        i = 0
        while i < len(name) and j < len(typed):
            if name[i] == typed[j]:
                j += 1
                i += 1
            elif i > 0 and typed[j] == name[i-1]:
                j += 1
            else:
                return False
        if i < len(name):
            return False
        i = len(name) - 1
        while j < len(typed):
            if name[i] != typed[j]:
                return False
            j += 1
        return True