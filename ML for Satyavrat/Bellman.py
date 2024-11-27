# Define the number of vertices and edges
V = 5
E = 8

# Define edges as a list of dictionaries
edges = [
    {"src": 0, "dest": 1, "weight": -1},
    {"src": 0, "dest": 2, "weight": 4},
    {"src": 1, "dest": 2, "weight": 3},
    {"src": 1, "dest": 3, "weight": 2},
    {"src": 1, "dest": 4, "weight": 2},
    {"src": 3, "dest": 2, "weight": 5},
    {"src": 3, "dest": 1, "weight": 1},
    {"src": 4, "dest": 3, "weight": -3},
]

def bellman_ford(edges, src, V):
    # Use a high value for "infinity"
    INF = 100000

    # Initialize distance array
    dist = [INF] * V
    dist[src] = 0

    # Relax all edges V-1 times
    for _ in range(V - 1):
        for edge in edges:
            u, v, weight = edge["src"], edge["dest"], edge["weight"]
            if dist[u] != INF and dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight

    # Check for negative weight cycle
    for edge in edges:
        u, v, weight = edge["src"], edge["dest"], edge["weight"]
        if dist[u] != INF and dist[u] + weight < dist[v]:
            print("Graph contains negative weight cycle")
            return

    # Print results
    print("Vertex \t Distance from Source")
    for i in range(V):
        print(f"{i} \t {dist[i]}")

# Run the Bellman-Ford algorithm
bellman_ford(edges, 0, V)
