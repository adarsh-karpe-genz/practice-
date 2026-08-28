/**
 * Problem: Graph Traversals (BFS & DFS)
 * 
 * Representation: Adjacency Matrix
 * Time Complexity: O(V^2) for Matrix (O(V + E) for List)
 * Space Complexity: O(V)
 */

#include <stdio.h>
#include <stdbool.h>

#define MAX_V 10

void bfs(int adj[MAX_V][MAX_V], int numVertices, int startVertex) {
    bool visited[MAX_V] = {false};
    int queue[MAX_V];
    int front = 0, rear = 0;

    visited[startVertex] = true;
    queue[rear++] = startVertex;

    printf("BFS Order: ");
    while (front < rear) {
        int curr = queue[front++];
        printf("%d ", curr);

        for (int i = 0; i < numVertices; i++) {
            if (adj[curr][i] && !visited[i]) {
                visited[i] = true;
                queue[rear++] = i;
            }
        }
    }
    printf("\n");
}

void dfsUtil(int adj[MAX_V][MAX_V], int numVertices, int vertex, bool visited[]) {
    visited[vertex] = true;
    printf("%d ", vertex);

    for (int i = 0; i < numVertices; i++) {
        if (adj[vertex][i] && !visited[i]) {
            dfsUtil(adj, numVertices, i, visited);
        }
    }
}

void dfs(int adj[MAX_V][MAX_V], int numVertices, int startVertex) {
    bool visited[MAX_V] = {false};
    printf("DFS Order: ");
    dfsUtil(adj, numVertices, startVertex, visited);
    printf("\n");
}

int main(void) {
    int adj[MAX_V][MAX_V] = {0};
    int numVertices = 5;

    // Edge connections
    adj[0][1] = adj[1][0] = 1;
    adj[0][2] = adj[2][0] = 1;
    adj[1][3] = adj[3][1] = 1;
    adj[1][4] = adj[4][1] = 1;

    printf("[C] Graph Traversals Test\n");
    bfs(adj, numVertices, 0);
    dfs(adj, numVertices, 0);
    return 0;
}
