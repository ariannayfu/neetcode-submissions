"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        graph = {}
        def dfs(curr: Optional['Node']) -> Optional['Node']:
            if curr in graph:
                return graph[curr]
            clone = Node()
            clone.val = curr.val
            graph[curr] = clone
            for pair in curr.neighbors:
                clone.neighbors.append(dfs(pair))
            return clone

        return dfs(node)



