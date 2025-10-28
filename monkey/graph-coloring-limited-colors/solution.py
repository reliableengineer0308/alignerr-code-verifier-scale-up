def can_color_graph(graph, k):
    """
    Determines if an undirected graph can be colored with at most k colors
    such that no adjacent vertices share the same color.

    Args:
        graph (dict): Adjacency list representation of undirected graph
                       e.g., {0: [1, 2], 1: [0], 2: [0]}
        k (int): Maximum number of colors allowed

    Returns:
        bool: True if coloring is possible, False otherwise
    """
    if not graph:
        return True  # Empty graph is always colorable

    vertices = list(graph.keys())
    n = len(vertices)

    # Special cases
    if k == 0:
        return False  # No colors available
    if k >= n:
        return True   # Each vertex can get unique color

    # Color array: -1 means uncolored
    colors = [-1] * n

    def is_safe(v, color):
        """Check if assigning 'color' to vertex 'v' is valid."""
        for neighbor in graph[v]:
            if colors[neighbor] == color:
                return False
        return True

    def backtrack(v):
        """Recursively assign colors to vertices starting from index v."""
        if v == n:
            return True  # All vertices colored

        vertex = vertices[v]
        # Try all colors from 0 to k-1
        for color in range(k):
            if is_safe(vertex, color):
                colors[vertex] = color
                if backtrack(v + 1):
                    return True
                # Backtrack
                colors[vertex] = -1
        return False

    return backtrack(0)
