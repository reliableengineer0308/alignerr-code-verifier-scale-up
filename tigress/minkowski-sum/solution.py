import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)
    
    def __eq__(self, other):
        return abs(self.x - other.x) < 1e-9 and abs(self.y - other.y) < 1e-9
    
    def __hash__(self):
        return hash((round(self.x, 9), round(self.y, 9)))
    
    def __lt__(self, other):
        if abs(self.y - other.y) < 1e-9:
            return self.x < other.x
        return self.y < other.y
    
    def __repr__(self):
        return f"({self.x}, {self.y})"

def cross(o, a, b):
    return (a.x - o.x) * (b.y - o.y) - (a.y - o.y) * (b.x - o.x)

class MinkowskiSum:
    def __init__(self):
        pass
    
    def convex_hull(self, points):
        if len(points) <= 1:
            return points
        
        # Remove duplicates
        unique_points = {}
        for p in points:
            unique_points[(round(p.x, 9), round(p.y, 9))] = p
        points = list(unique_points.values())
        
        if len(points) <= 1:
            return points
        
        points.sort(key=lambda p: (p.y, p.x))
        
        def build_hull(points):
            hull = []
            for p in points:
                while len(hull) >= 2 and cross(hull[-2], hull[-1], p) <= 0:
                    hull.pop()
                hull.append(p)
            return hull
        
        lower = build_hull(points)
        upper = build_hull(reversed(points))
        return lower[:-1] + upper[:-1]
    
    def minkowski_sum(self, polyA, polyB):
        # For convex polygons, Minkowski sum can be computed by merging edges
        sum_points = []
        
        # Generate all pairwise sums
        for pointA in polyA:
            for pointB in polyB:
                sum_points.append(pointA + pointB)
        
        # Return convex hull of the sums
        return self.convex_hull(sum_points)

def solve_minkowski_sum():
    import sys
    input = sys.stdin.read().split()
    idx = 0
    
    # Read polygon A
    n = int(input[idx]); idx += 1
    polyA = []
    for _ in range(n):
        x = float(input[idx]); y = float(input[idx+1]); idx += 2
        polyA.append(Point(x, y))
    
    # Read polygon B
    m = int(input[idx]); idx += 1
    polyB = []
    for _ in range(m):
        x = float(input[idx]); y = float(input[idx+1]); idx += 2
        polyB.append(Point(x, y))
    
    # Compute Minkowski sum
    solver = MinkowskiSum()
    result_poly = solver.minkowski_sum(polyA, polyB)
    
    # Output results
    results = [str(len(result_poly))]
    for point in result_poly:
        results.append(f"{int(point.x) if point.x.is_integer() else point.x} {int(point.y) if point.y.is_integer() else point.y}")
    
    return results