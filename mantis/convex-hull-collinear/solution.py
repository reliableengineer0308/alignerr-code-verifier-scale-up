import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __lt__(self, other):
        if self.y == other.y:
            return self.x < other.x
        return self.y < other.y
    
    def __hash__(self):
        return hash((self.x, self.y))
    
    def __repr__(self):
        return f"({self.x}, {self.y})"

def cross(o, a, b):
    return (a.x - o.x) * (b.y - o.y) - (a.y - o.y) * (b.x - o.x)

def distance_sq(a, b):
    return (a.x - b.x)**2 + (a.y - b.y)**2

class ConvexHull:
    def __init__(self):
        pass
    
    def convex_hull_with_collinear(self, points):
        if len(points) <= 1:
            return points
        
        # Remove duplicates
        points = list(set(points))
        
        if len(points) == 1:
            return points
        
        # Find the point with the lowest y (and leftmost if tie)
        start = min(points, key=lambda p: (p.y, p.x))
        
        # Sort points by polar angle relative to start point
        def sort_key(p):
            if p == start:
                return (-float('inf'), 0)
            angle = math.atan2(p.y - start.y, p.x - start.x)
            dist = distance_sq(start, p)
            return (angle, dist)
        
        sorted_points = sorted(points, key=sort_key)
        
        # Build hull using monotone chain with collinear handling
        hull = [start]
        
        for i in range(1, len(sorted_points)):
            while len(hull) >= 2:
                # Check if points are collinear or making a right turn
                orientation = cross(hull[-2], hull[-1], sorted_points[i])
                if orientation < 0:
                    # Right turn - remove last point
                    hull.pop()
                elif orientation == 0:
                    # Collinear - keep the farther point
                    if distance_sq(hull[-2], sorted_points[i]) > distance_sq(hull[-2], hull[-1]):
                        hull.pop()
                    else:
                        break
                else:
                    # Left turn - keep the point
                    break
            hull.append(sorted_points[i])
        
        # Now include all collinear points that lie on hull edges
        final_hull = []
        n = len(hull)
        
        for i in range(n):
            current = hull[i]
            next_point = hull[(i + 1) % n]
            final_hull.append(current)
            
            # Find all points collinear with current and next_point
            collinear_points = []
            for p in points:
                if p != current and p != next_point and cross(current, next_point, p) == 0:
                    # Check if p lies on the segment between current and next_point
                    if (min(current.x, next_point.x) <= p.x <= max(current.x, next_point.x) and
                        min(current.y, next_point.y) <= p.y <= max(current.y, next_point.y)):
                        collinear_points.append(p)
            
            # Sort collinear points by distance from current point
            collinear_points.sort(key=lambda p: distance_sq(current, p))
            final_hull.extend(collinear_points)
        
        # Remove duplicates while preserving order
        seen = set()
        unique_hull = []
        for p in final_hull:
            if p not in seen:
                seen.add(p)
                unique_hull.append(p)
        
        return unique_hull

def solve_convex_hull():
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
        
        hull_solver = ConvexHull()
        hull_points = hull_solver.convex_hull_with_collinear(points)
        
        results.append(f"Case #{case_num}: {len(hull_points)}")
        for p in hull_points:
            results.append(f"{p.x} {p.y}")
    
    return results
