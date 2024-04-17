import heapq

# Define the river network as a graph using adjacency list representation
river_network = {
    'A': {'B': 5, 'C': 3},
    'B': {'A': 5, 'D': 4, 'E': 2},
    'C': {'A': 3, 'E': 6},
    'D': {'B': 4, 'E': 3},
    'E': {'B': 2, 'C': 6, 'D': 3}
}

def dijkstra_shortest_path(graph, start, end):
    # Priority queue to store nodes with the minimum distance from the start
    min_heap = []
    heapq.heappush(min_heap, (0, start))  # (distance, node)
    
    # Dictionary to keep track of the shortest distance from start to each node
    shortest_distance = {node: float('inf') for node in graph}
    shortest_distance[start] = 0
    
    # Dictionary to store the previous node in the shortest path
    previous_node = {node: None for node in graph}
    
    while min_heap:
        current_distance, current_node = heapq.heappop(min_heap)
        
        if current_node == end:
            break
        
        if current_distance > shortest_distance[current_node]:
            continue
        
        for neighbor, distance in graph[current_node].items():
            new_distance = current_distance + distance
            if new_distance < shortest_distance[neighbor]:
                shortest_distance[neighbor] = new_distance
                previous_node[neighbor] = current_node
                heapq.heappush(min_heap, (new_distance, neighbor))
    
    # Reconstruct the shortest path from start to end
    path = []
    node = end
    while node is not None:
        path.append(node)
        node = previous_node[node]
    path.reverse()
    
    return path, shortest_distance[end]

# Find the shortest path from node 'A' to node 'E'
start_node = 'A'
end_node = 'E'
shortest_path, shortest_distance = dijkstra_shortest_path(river_network, start_node, end_node)

print(f"Shortest Path from {start_node} to {end_node}: {' -> '.join(shortest_path)}")
print(f"Shortest Distance: {shortest_distance} units")
