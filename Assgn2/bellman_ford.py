def bellman_ford(graph, source):
    # Find number of nodes in graph
    num_nodes = max(max(node1, node2) for node1, node2, _ in graph)

    # Initialize distance vectors as infinity and set distance to self as 0
    distance = {index + 1: float('inf') for index in range(num_nodes)}
    distance[source] = 0

    # Update distance vector 
    for source, destination, cost in graph:
        if distance[source] < distance[destination] and distance[source] + cost < distance[destination]:
            distance[destination] = distance[source] + cost

    # Checking for negative weights
    for source, destination, cost in graph:
        if distance[source] + cost < distance[destination]:
            return "Graph contains negative weight cycle"
            
    return distance

# Test the function with Figure 1 
# (source, destination, cost)
graph1 = [
    (1, 2, 2),
    (1, 3, 7),
    (2, 3, 1),
]

# Graph two with negative cycles (Figure 2)
graph2 = [
    (1, 2, -2),
    (2, 3, -2),
    (3, 1, 1),
]

# Graph three with 5 nodes (Figure 3)
graph3 = [
    (1, 3, 5),
    (1, 2, 3),
    (3, 4, 4),
    (4, 5, 2),
    (5, 2, 7),
    (2, 4, 6),
]

# Testing
source = 1
print("\nFrom node:", source)
print("To nodes:", bellman_ford(graph3, source))