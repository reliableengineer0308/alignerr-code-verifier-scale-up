from collections import deque

def topological_sort(graph):
    """
    Performs topological sort on a directed graph using Kahn's algorithm.
    
    Args:
        graph (dict): Adjacency list representation of directed graph
                     e.g., {"A": ["B"], "B": []}
    
    Returns:
        list: Topologically sorted nodes if DAG, else empty list if cycle exists
    """
    if not graph:
        return []
    
    # Step 1: Compute indegree for each node
    indegree = {node: 0 for node in graph}
    for node in graph:
        for neighbor in graph[node]:
            if neighbor in indegree:
                indegree[neighbor] += 1
            else:
                # Add missing node (with no outgoing edges) to indegree
                indegree[neighbor] = 1

    # Step 2: Initialize queue with nodes of indegree 0
    queue = deque([node for node, deg in indegree.items() if deg == 0])
    result = []

    # Step 3: Process nodes
    while queue:
        node = queue.popleft()
        result.append(node)

        # Reduce indegree of all neighbors
        for neighbor in graph.get(node, []):
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    # Step 4: Check for cycles
    if len(result) != len(indegree):
        return []  # Cycle detected

    return result
