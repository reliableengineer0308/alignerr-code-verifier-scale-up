class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __repr__(self):
        return f"({self.x}, {self.y})"

class PolygonPointLocation:
    def __init__(self, vertices):
        self.vertices = [Point(x, y) for x, y in vertices]
        self.n = len(vertices)
    
    def update_vertex(self, index, new_x, new_y):
        self.vertices[index] = Point(new_x, new_y)
    
    def point_on_segment(self, p, a, b):
        """Check if point p lies on segment ab"""
        # Check if p is collinear with a and b
        cross_product = (p.y - a.y) * (b.x - a.x) - (p.x - a.x) * (b.y - a.y)
        if abs(cross_product) > 1e-9:
            return False
        
        # Check if p is between a and b
        if min(a.x, b.x) <= p.x <= max(a.x, b.x) and min(a.y, b.y) <= p.y <= max(a.y, b.y):
            return True
        return False
    
    def query_point(self, x, y):
        query_point = Point(x, y)
        
        # First check if point is on boundary
        for i in range(self.n):
            a = self.vertices[i]
            b = self.vertices[(i + 1) % self.n]
            if self.point_on_segment(query_point, a, b):
                return "BOUNDARY"
        
        # Ray casting algorithm
        inside = False
        for i in range(self.n):
            a = self.vertices[i]
            b = self.vertices[(i + 1) % self.n]
            
            # Check if ray crosses edge
            if ((a.y > query_point.y) != (b.y > query_point.y)) and \
               (query_point.x < (b.x - a.x) * (query_point.y - a.y) / (b.y - a.y) + a.x):
                inside = not inside
        
        return "INSIDE" if inside else "OUTSIDE"

def solve_polygon_point_location():
    import sys
    input = sys.stdin.read().split()
    idx = 0
    
    # Read initial polygon
    n = int(input[idx]); idx += 1
    vertices = []
    for _ in range(n):
        x = float(input[idx]); y = float(input[idx+1]); idx += 2
        vertices.append((x, y))
    
    # Create polygon
    polygon = PolygonPointLocation(vertices)
    
    # Read operations
    q = int(input[idx]); idx += 1
    results = []
    
    for _ in range(q):
        op_type = input[idx]; idx += 1
        if op_type == "QUERY":
            x = float(input[idx]); y = float(input[idx+1]); idx += 2
            result = polygon.query_point(x, y)
            results.append(result)
        elif op_type == "UPDATE":
            i = int(input[idx]); x = float(input[idx+1]); y = float(input[idx+2]); idx += 3
            polygon.update_vertex(i, x, y)
    
    return results

if __name__ == '__main__':
    results = solve_polygon_point_location()
    for result in results:
        print(result)