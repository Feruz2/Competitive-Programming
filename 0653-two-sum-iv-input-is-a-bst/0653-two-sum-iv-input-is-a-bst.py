# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findnext(self, nextt):
            if nextt:
                num = nextt.pop()
                if num.right:
                    node = num.right
                    nextt.append(node)
                    while node:
                        if node.left:
                            node = node.left
                            nextt.append(node)
                        else:
                            break

                return num.val
    def findprev(self, prev):
            if prev:
                num = prev.pop()
                if num.left:
                    node = num.left
                    prev.append(node)
                    while node:
                        if node.right:
                            node = node.right
                            prev.append(node)
                        else:
                            break
                return num.val
        
        

    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        nextt = [root]
        node = root
        
        while node:
            if node.left:
                node = node.left
                nextt.append(node)
            else:
                break
        
        prev = [root]
        node = root
        while node:
            if node.right:
                node = node.right
                prev.append(node)
                
            else:
                break
        left = self.findnext(nextt)
        right = self.findprev(prev)
        
        while left != right:
            if left + right == k: 
                return True
            elif left + right > k:
                right = self.findprev(prev)
            else:
                left = self.findnext(nextt)
                
        return False
            
        
        