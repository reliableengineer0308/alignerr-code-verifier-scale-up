def canFinish(numCourses: int, prerequisites: list[list[int]]) -> bool:
    """
    Determines if all courses can be finished using topological sort (DFS).
    Time: O(V + E), Space: O(V + E)
    """
    # Build adjacency list
    graph = {i: [] for i in range(numCourses)}
    for course, prereq in prerequisites:
        graph[prereq].append(course)
    
    
    # Track visited states: 0=unvisited, 1=visiting (in current DFS path), 2=visited
    visited = [0] * numCourses
    
    def hasCycle(course: int) -> bool:
        if visited[course] == 1:  # Already in current path → cycle
            return True
        if visited[course] == 2:  # Already processed
            return False
        
        visited[course] = 1  # Mark as visiting
        
        for neighbor in graph[course]:
            if hasCycle(neighbor):
                return True
        
        visited[course] = 2  # Mark as visited
        return False
    
    
    # Check each course for cycles
    for course in range(numCourses):
        if hasCycle(course):
            return False  # Cycle found → impossible to finish
    
    return True  # No cycles → all courses can be finished
