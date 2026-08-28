"""
Problem: Graph Traversals (BFS & DFS)

Representation: Adjacency List (Dict of Lists)
Time Complexity: O(V + E)
Space Complexity: O(V + E)
"""

from collections import deque
from typing import Dict, List

class Graph:
    def __init__(self):
        self.adj: Dict[int, List[int]] = {}

    def add_edge(self, u: int, v: int):
        self.adj.setdefault(u, []).append(v)
        self.adj.setdefault(v, []).append(u)

    def bfs(self, start: int) -> List[int]:
        visited = set([start])
        queue = deque([start])
        order = []

        while queue:
            node = queue.popleft()
            order.append(node)
            for neighbor in self.adj.get(node, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return order

    def dfs(self, start: int) -> List[int]:
        visited = set()
        order = []

        def _dfs(node):
            visited.add(node)
            order.append(node)
            for neighbor in self.adj.get(node, []):
                if neighbor not in visited:
                    _dfs(neighbor)

        _dfs(start)
        return order

if __name__ == "__main__":
    print("[Python] Graph Traversals Test")
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(1, 4)

    bfs_res = g.bfs(0)
    dfs_res = g.dfs(0)
    print("BFS Order:", bfs_res)
    print("DFS Order:", dfs_res)
    assert len(bfs_res) == 5
    assert len(dfs_res) == 5
    print("Graph traversals test passed!")
