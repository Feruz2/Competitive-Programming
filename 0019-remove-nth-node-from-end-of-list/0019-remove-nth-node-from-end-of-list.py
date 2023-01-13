# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def fun(node):
            if not node.next:
                return 1
            x = fun(node.next)
            if x == 0:
                return 0
            if x == n:
                if node.next.next:
                    node.next = node.next.next
                else:
                    node.next = None
                return 0
            return x+1
        
        temp = head
        x = fun(temp)
        # print(x)
        if x != 0:
            return head.next
            
        return head
    
   