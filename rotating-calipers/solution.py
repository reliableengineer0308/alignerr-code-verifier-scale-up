import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __hash__(self):
        return hash((self.x, self.y))
    
    def __lt__(self, other):
        if self.y == other.y:
            return self.x < other.x
        return self.y < other.y
    
    def __repr__(self):
        return f"({self.x}, {self.y})"

def cross(o, a, b):
    return (a.x - o.x) * (b.y - o.y) - (a.y - o.y) * (b.x - o.x)

def distance_sq(a, b):
    return (a.x - b.x)**2 + (a.y - b.y)**2

class RotatingCalipers:
    def __init__(self):
        pass
    
    def convex_hull(self, points):
        if len(points) <= 1:
            return points
        
        # Remove duplicates using dictionary (since points may not be hashable in some implementations)
        unique_points = {}
        for p in points:
            unique_points[(p.x, p.y)] = p
        points = list(unique_points.values())
        
        if len(points) <= 1:
            return points
        
        # Sort points by y, then x
        points.sort(key=lambda p: (p.y, p.x))
        
        # Build lower hull
        lower = []
        for p in points:
            while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
                lower.pop()
            lower.append(p)
        
        # Build upper hull  
        upper = []
        for p in reversed(points):
            while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
                upper.pop()
            upper.append(p)
        
        # Remove duplicates at connection points
        return lower[:-1] + upper[:-1]
    
    def maximum_distance(self, points):
        if len(points) == 1:
            return 0, points[0], points[0]
        if len(points) == 2:
            return distance_sq(points[0], points[1]), points[0], points[1]
        
        # Compute convex hull
        hull = self.convex_hull(points)
        n = len(hull)
        
        if n == 1:
            return 0, hull[0], hull[0]
        if n == 2:
            return distance_sq(hull[0], hull[1]), hull[0], hull[1]
        
        # Use rotating calipers algorithm
        max_dist_sq = 0
        p1, p2 = hull[0], hull[0]
        
        # Start from leftmost point
        i = 0
        j = 1
        
        while i < n:
            # Current distance
            current_dist = distance_sq(hull[i], hull[j])
            if current_dist > max_dist_sq:
                max_dist_sq = current_dist
                p1, p2 = hull[i], hull[j]
            
            # Next j candidate
            next_j = (j + 1) % n
            
            # Calculate cross products to decide which pointer to move
            vec1 = hull[(i + 1) % n] - hull[i]
            vec2 = hull[next_j] - hull[j]
            
            cross_product = vec1.x * vec2.y - vec1.y * vec2.x
            
            if cross_product >= 0:
                j = next_j
            else:
                i += 1
                if i == j:
                    j = (j + 1) % n
        
        return max_dist_sq, p1, p2

def solve_rotating_calipers():
    import sys
    input = sys.stdin.read().split()
    t = int(input[0])
    idx = 1
    results = []
    
    for case_num in range(1, t + 1):
        n = int(input[idx]); idx += 1
        points = []
        for i in range(n):
            x = int(input[idx]); y = int(input[idx+1]); idx += 2
            points.append(Point(x, y))
        
        solver = RotatingCalipers()
        max_dist_sq, p1, p2 = solver.maximum_distance(points)
        
        results.append(f"Case #{case_num}: {max_dist_sq}")
        results.append(f"{p1.x} {p1.y}")
        results.append(f"{p2.x} {p2.y}")
    
    return results
