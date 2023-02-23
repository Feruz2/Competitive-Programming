class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        A, B, C, D = rec1[0], rec1[1] ,rec1[2], rec1[3]
        E, F, G, H = rec2[0], rec2[1] ,rec2[2], rec2[3]
        left = max(A, E)
        right = min(G, C)
        bottom = max(F, B)
        top = min(D, H)
        if right > left and top > bottom:
            return True
        return False
 