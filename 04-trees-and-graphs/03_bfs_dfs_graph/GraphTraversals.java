/**
 * Problem: Graph Traversals (BFS & DFS)
 * 
 * Representation: Adjacency List
 * Time Complexity: O(V + E)
 * Space Complexity: O(V + E)
 */

import java.util.*;

public class GraphTraversals {
    private final int V;
    private final List<List<Integer>> adj;

    public GraphTraversals(int v) {
        this.V = v;
        adj = new ArrayList<>(v);
        for (int i = 0; i < v; i++) adj.add(new ArrayList<>());
    }

    public void addEdge(int u, int v) {
        adj.get(u).add(v);
        adj.get(v).add(u);
    }

    public void bfs(int start) {
        boolean[] visited = new boolean[V];
        Queue<Integer> queue = new LinkedList<>();

        visited[start] = true;
        queue.add(start);

        System.out.print("BFS: ");
        while (!queue.isEmpty()) {
            int curr = queue.poll();
            System.out.print(curr + " ");

            for (int neighbor : adj.get(curr)) {
                if (!visited[neighbor]) {
                    visited[neighbor] = true;
                    queue.add(neighbor);
                }
            }
        }
        System.out.println();
    }

    private void dfsUtil(int curr, boolean[] visited) {
        visited[curr] = true;
        System.out.print(curr + " ");

        for (int neighbor : adj.get(curr)) {
            if (!visited[neighbor]) {
                dfsUtil(neighbor, visited);
            }
        }
    }

    public void dfs(int start) {
        boolean[] visited = new boolean[V];
        System.out.print("DFS: ");
        dfsUtil(start, visited);
        System.out.println();
    }

    public static void main(String[] args) {
        System.out.println("[Java] Graph Traversals Test");
        GraphTraversals g = new GraphTraversals(5);
        g.addEdge(0, 1);
        g.addEdge(0, 2);
        g.addEdge(1, 3);
        g.addEdge(1, 4);

        g.bfs(0);
        g.dfs(0);
    }
}
