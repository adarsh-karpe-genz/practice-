/**
 * Problem: Graph Traversals (BFS & DFS)
 * 
 * Representation: Adjacency List
 * Time Complexity: O(V + E)
 * Space Complexity: O(V + E)
 */

#include <iostream>
#include <vector>
#include <queue>

class Graph {
    int V;
    std::vector<std::vector<int>> adj;

    void dfsUtil(int v, std::vector<bool>& visited) {
        visited[v] = true;
        std::cout << v << " ";
        for (int neighbor : adj[v]) {
            if (!visited[neighbor]) {
                dfsUtil(neighbor, visited);
            }
        }
    }

public:
    Graph(int v) : V(v), adj(v) {}

    void addEdge(int u, int v) {
        adj[u].push_back(v);
        adj[v].push_back(u); // undirected
    }

    void bfs(int start) {
        std::vector<bool> visited(V, false);
        std::queue<int> q;

        visited[start] = true;
        q.push(start);

        std::cout << "BFS: ";
        while (!q.empty()) {
            int u = q.front();
            q.pop();
            std::cout << u << " ";

            for (int v : adj[u]) {
                if (!visited[v]) {
                    visited[v] = true;
                    q.push(v);
                }
            }
        }
        std::cout << "\n";
    }

    void dfs(int start) {
        std::vector<bool> visited(V, false);
        std::cout << "DFS: ";
        dfsUtil(start, visited);
        std::cout << "\n";
    }
};

int main() {
    std::cout << "[C++] Graph Traversals Test\n";
    Graph g(5);
    g.addEdge(0, 1);
    g.addEdge(0, 2);
    g.addEdge(1, 3);
    g.addEdge(1, 4);

    g.bfs(0);
    g.dfs(0);
    return 0;
}
