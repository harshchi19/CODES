# Define the number of vertices
V = 4

def min_distance(dist, visited):
    # Initialize minimum value
    min_value = 100000
    min_index = -1

    for v in range(V):
        if not visited[v] and dist[v] <= min_value:
            min_value = dist[v]
            min_index = v
    return min_index

def dijkstra(graph, src):
    # Use a high value for "infinity"
    INF = 100000

    # Initialize distance array and visited set
    dist = [INF] * V
    visited = [False] * V

    # Distance to the source itself is always 0
    dist[src] = 0

    for _ in range(V - 1):
        # Pick the minimum distance vertex from the set of vertices not yet processed
        u = min_distance(dist, visited)

        # Mark the vertex as processed
        visited[u] = True

        # Update distance values of adjacent vertices of the picked vertex
        for v in range(V):
            if (
                graph[u][v] > 0 and  # Edge exists
                not visited[v] and  # Not already visited
                dist[u] != INF and  # Source vertex distance is not INF
                dist[u] + graph[u][v] < dist[v]  # Update condition
            ):
                dist[v] = dist[u] + graph[u][v]

    # Print the results
    print("Vertex \t Distance from Source")
    for i in range(V):
        print(f"{i} \t {dist[i]}")

# Adjacency matrix representation of the graph
graph = [
    [0, 1, 4, 0],
    [1, 0, 2, 6],
    [4, 2, 0, 3],
    [0, 6, 3, 0]
]

# Run Dijkstra's algorithm
start_vertex = 0
dijkstra(graph, start_vertex)
