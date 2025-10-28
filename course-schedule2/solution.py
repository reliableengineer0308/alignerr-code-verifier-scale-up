from collections import deque, defaultdict

def can_finish_courses(num_courses, prerequisites):
    """
    Check if all courses can be finished using topological sort
    """
    # Build graph and indegree array
    graph = defaultdict(list)
    indegree = [0] * num_courses
    
    for course, prereq in prerequisites:
        graph[prereq].append(course)
        indegree[course] += 1
    
    # Topological sort using Kahn's algorithm
    queue = deque()
    for i in range(num_courses):
        if indegree[i] == 0:
            queue.append(i)
    
    count = 0
    while queue:
        course = queue.popleft()
        count += 1
        
        for neighbor in graph[course]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    
    return count == num_courses