def find_critical_node_components(n: int, edges: list) -> list:
    """
    Find critical nodes (articulation points) and compute connected components 
    after removing each critical node.

    Args:
        n: number of nodes (0 to n-1)
        edges: list of (u, v) tuples representing undirected edges

    Returns:
        List of (node, component_count) sorted by node
    """
    from collections import defaultdict, deque

    # Build adjacency list
    adj = defaultdict(list)
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    # Step 1: Find articulation points using DFS
    disc = [-1] * n  # Discovery time
    low = [-1] * n   # Lowest discovery time reachable
    parent = [-1] * n
    visited = [False] * n
    is_articulation = [False] * n

    time = 0

    def dfs(u):
        nonlocal time
        children = 0
        disc[u] = low[u] = time
        time += 1
        visited[u] = True

        for v in adj[u]:
            if not visited[v]:
                parent[v] = u
                children += 1
                dfs(v)

                low[u] = min(low[u], low[v])

                # Condition 1: u is root with at least 2 children
                if parent[u] == -1 and children > 1:
                    is_articulation[u] = True
                # Condition 2: u is not root and low[v] >= disc[u]
                if parent[u] != -1 and low[v] >= disc[u]:
                    is_articulation[u] = True
            elif v != parent[u]:  # Back edge
                low[u] = min(low[u], disc[v])


    for i in range(n):
        if not visited[i]:
            dfs(i)

    critical_nodes = [i for i in range(n) if is_articulation[i]]


    # Step 2: For each critical node, compute components after removal
    result = []

    for node in critical_nodes:
        # Create graph without 'node'
        remaining_nodes = set(range(n)) - {node}
        if not remaining_nodes:
            result.append((node, 0))
            continue

        # Build subgraph adjacency
        sub_adj = defaultdict(list)
        for u in remaining_nodes:
            for v in adj[u]:
                if v in remaining_nodes:
                    sub_adj[u].append(v)


        # Count connected components using BFS
        visited_sub = set()
        components = 0

        for start in remaining_nodes:
            if start not in visited_sub:
                components += 1
                queue = deque([start])
                visited_sub.add(start)

                while queue:
                    u = queue.popleft()
                    for v in sub_adj[u]:
                        if v not in visited_sub:
                            visited_sub.add(v)
                            queue.append(v)

        result.append((node, components))


    # Sort by node ID
    return sorted(result, key=lambda x: x[0])
