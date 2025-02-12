def depth_first_search(graph, start, visited=None):
    if visited is None:
        visited = set()
    
    # Mark the current node as visited
    visited.add(start)
    print(start)  # Process the node (e.g., print it)

    # Recur for all the vertices adjacent to this vertex
    for neighbor in graph[start]:
        if neighbor not in visited:
            depth_first_search(graph, neighbor, visited)
    
    return visited

# Example usage:
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

depth_first_search(graph, 'A')
