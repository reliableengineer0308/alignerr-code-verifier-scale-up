from collections import deque, defaultdict
import math

def minimizeTotalDelay(n, m, processing_time, dependencies):
    """
    Returns minimum makespan to complete all tasks with resource allocation.
    Time: O(n^2 * m), Space: O(n + edges)
    """
    # Build graph and in-degree count
    graph = defaultdict(list)
    in_degree = [0] * n
    
    for i, deps in enumerate(dependencies):
        for d in deps:
            graph[d].append(i)  # FIXED: was graphd.append(i)
            in_degree[i] += 1  # FIXED: was in_degreei += 1


    # Topological order
    topo_order = []
    q = deque([i for i in range(n) if in_degree[i] == 0])  # FIXED: in_degree[i]
    while q:
        u = q.popleft()
        topo_order.append(u)
        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                q.append(v)


    # Earliest start time for each task
    start_time = [0] * n

    for task in topo_order:
        # Start only after all dependencies complete
        if dependencies[task]:
            start_time[task] = max(start_time[dep] for dep in dependencies[task])


        # Try all possible resource allocations (1 to m)
        best_finish = float('inf')
        for k in range(1, m + 1):
            duration = math.ceil(processing_time[task] / k)
            finish = start_time[task] + duration
            best_finish = min(best_finish, finish)


        start_time[task] = best_finish  # This is finish time (correct by design)


    return max(start_time)  # Makespan
