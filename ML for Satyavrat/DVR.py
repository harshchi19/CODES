# Define global variables
dist = []
temp = []
n = 0

def dvr():
    global dist, temp, n
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    temp[i][j] = k

    # Display the state value for each router
    for i in range(n):
        print(f"\n\nState value for router {i + 1} is:")
        for j in range(n):
            print(f"  Node {j + 1} via {temp[i][j] + 1} distance {dist[i][j]}")

def main():
    global dist, temp, n
    n = int(input("Enter the number of nodes: "))
    
    # Initialize distance and temp matrices
    dist = [[0] * n for _ in range(n)]
    temp = [[0] * n for _ in range(n)]
    
    print("Enter distance matrix:")
    for i in range(n):
        for j in range(n):
            dist[i][j] = int(input(f"Enter distance from {i + 1} to {j + 1}: "))
            if i == j:
                dist[i][j] = 0  # Distance to self is 0
            temp[i][j] = j

    dvr()

    # Update the distance matrix
    i = int(input("Enter value of i (source node index): ")) - 1
    j = int(input("Enter value of j (destination node index): ")) - 1
    x = int(input("Enter cost to update: "))
    dist[i][j] = x

    print("After update:")
    dvr()

if __name__ == "__main__":
    main()
