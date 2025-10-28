def has_cycle(graph):
    """
    Detects if a directed graph has a cycle using DFS with three-color marking.
    
    Args:
        graph: dict, adjacency list representation of directed graph
               e.g., {"A": ["B"], "B": ["C"]}
    Returns:
        bool: True if cycle exists, False otherwise
    """
    if not graph:
        return False

    # Track state of each node: 0=unvisited, 1=visiting, 2=visited
    state = {node: 0 for node in graph}


    def dfs(node):
        # Mark as currently visiting
        state[node] = 1

        # Explore neighbors
        for neighbor in graph.get(node, []):
            if state[neighbor] == 1:
                # Found back edge to a node in current path → cycle
                return True
            if state[neighbor] == 0:
                # Unvisited neighbor → recurse
                if dfs(neighbor):
                    return True

        # Mark as fully visited
        state[node] = 2
        return False

    # Check each node (for disconnected graphs)
    for node in graph:
        if state[node] == 0:  # Unvisited node
            if dfs(node):
                return True


    return False
