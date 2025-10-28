import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __eq__(self, other):
        return abs(self.x - other.x) < 1e-9 and abs(self.y - other.y) < 1e-9
    
    def __hash__(self):
        return hash((round(self.x, 9), round(self.y, 9)))
    
    def __repr__(self):
        return f"({self.x}, {self.y})"

def cross(o, a, b):
    return (a.x - o.x) * (b.y - o.y) - (a.y - o.y) * (b.x - o.x)

def dot(a, b):
    return a.x * b.x + a.y * b.y

class PolygonIntersection:
    def __init__(self):
        pass
    
    def polygon_area(self, points):
        """Calculate area of polygon using shoelace formula"""
        if len(points) < 3:
            return 0.0
        
        area = 0.0
        n = len(points)
        for i in range(n):
            j = (i + 1) % n
            area += points[i].x * points[j].y
            area -= points[j].x * points[i].y
        return abs(area) / 2.0
    
    def line_intersection(self, a1, a2, b1, b2):
        """Find intersection point of two line segments"""
        # Line AB represented as a1x + b1y = c1
        A1 = a2.y - a1.y
        B1 = a1.x - a2.x
        C1 = A1 * a1.x + B1 * a1.y
        
        # Line CD represented as a2x + b2y = c2
        A2 = b2.y - b1.y
        B2 = b1.x - b2.x
        C2 = A2 * b1.x + B2 * b1.y
        
        determinant = A1 * B2 - A2 * B1
        
        if abs(determinant) < 1e-9:
            return None  # Lines are parallel
        
        x = (B2 * C1 - B1 * C2) / determinant
        y = (A1 * C2 - A2 * C1) / determinant
        
        # Check if intersection point is within both segments
        def point_on_segment(p, a, b):
            return (min(a.x, b.x) - 1e-9 <= p.x <= max(a.x, b.x) + 1e-9 and
                    min(a.y, b.y) - 1e-9 <= p.y <= max(a.y, b.y) + 1e-9)
        
        if (point_on_segment(Point(x, y), a1, a2) and 
            point_on_segment(Point(x, y), b1, b2)):
            return Point(x, y)
        
        return None
    
    def point_inside_polygon(self, point, polygon):
        """Check if point is inside convex polygon using cross product method"""
        n = len(polygon)
        if n < 3:
            return False
        
        # For convex polygon, check if point is on same side of all edges
        sign = None
        for i in range(n):
            a = polygon[i]
            b = polygon[(i + 1) % n]
            cross_val = cross(a, b, point)
            
            if abs(cross_val) < 1e-9:
                # Point is on the line - check if it's on the segment
                if (min(a.x, b.x) - 1e-9 <= point.x <= max(a.x, b.x) + 1e-9 and
                    min(a.y, b.y) - 1e-9 <= point.y <= max(a.y, b.y) + 1e-9):
                    return True  # On boundary
                continue
            
            if sign is None:
                sign = 1 if cross_val > 0 else -1
            elif (cross_val > 0 and sign == -1) or (cross_val < 0 and sign == 1):
                return False
        
        return True
    
    def convex_polygon_intersection(self, polyA, polyB):
        """Compute intersection of two convex polygons using simple method"""
        intersection_points = []
        
        # Add all points of A that are inside B
        for point in polyA:
            if self.point_inside_polygon(point, polyB):
                intersection_points.append(point)
        
        # Add all points of B that are inside A
        for point in polyB:
            if self.point_inside_polygon(point, polyA):
                intersection_points.append(point)
        
        # Add all intersection points of edges
        for i in range(len(polyA)):
            a1 = polyA[i]
            a2 = polyA[(i + 1) % len(polyA)]
            
            for j in range(len(polyB)):
                b1 = polyB[j]
                b2 = polyB[(j + 1) % len(polyB)]
                
                intersection = self.line_intersection(a1, a2, b1, b2)
                if intersection:
                    intersection_points.append(intersection)
        
        # Remove duplicates
        unique_points = []
        for p in intersection_points:
            if not any(abs(p.x - q.x) < 1e-9 and abs(p.y - q.y) < 1e-9 for q in unique_points):
                unique_points.append(p)
        
        # If no intersection points, check if one polygon is completely inside the other
        if not unique_points:
            if all(self.point_inside_polygon(p, polyB) for p in polyA):
                return polyA
            elif all(self.point_inside_polygon(p, polyA) for p in polyB):
                return polyB
            return []  # No intersection
        
        # Sort points in counter-clockwise order for convex hull
        if len(unique_points) >= 3:
            # Find centroid
            cx = sum(p.x for p in unique_points) / len(unique_points)
            cy = sum(p.y for p in unique_points) / len(unique_points)
            centroid = Point(cx, cy)
            
            # Sort by angle relative to centroid
            unique_points.sort(key=lambda p: math.atan2(p.y - centroid.y, p.x - centroid.x))
        
        return unique_points
    
    def intersection_area(self, polyA, polyB):
        intersection_poly = self.convex_polygon_intersection(polyA, polyB)
        return self.polygon_area(intersection_poly)

def solve_polygon_intersection():
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
    
    # Compute intersection area
    solver = PolygonIntersection()
    area = solver.intersection_area(polyA, polyB)
    
    return [f"{area:.2f}"]