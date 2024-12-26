# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        ans = []
        st = []
        node = root
        while st or node:
            while node:
                st.append(node)
                node = node.left
            curr = st.pop()
            ans.append(curr.val)
            node = curr.right
        l = 0
        r = len(ans) - 1
        while l < r:
            curr = ans[l] + ans[r]
            if curr == k:
                return True
            if curr > k:
                r -= 1
            else:
                l += 1
        return False
            
            
        