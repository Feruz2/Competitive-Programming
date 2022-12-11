"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        
        qu = deque([(node,-1)])
        hash_map = defaultdict()
        
        while qu:
            N = len(qu)
            
            for i in range(N):
                
                curr,par = qu.popleft()
                if curr in hash_map:
                    continue
                new = Node(curr.val)
                hash_map[curr] = new
                
                for nextt in curr.neighbors:
                    if nextt.val != par:
                        qu.append((nextt,curr.val))
                        
        for key in hash_map:
            for nextt in key.neighbors:
                hash_map[key].neighbors.append(hash_map[nextt])
        return hash_map[node]