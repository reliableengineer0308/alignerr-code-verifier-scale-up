import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)
    
    def __eq__(self, other):
        return abs(self.x - other.x) < 1e-9 and abs(self.y - other.y) < 1e-9
    
    def __hash__(self):
        return hash((round(self.x, 9), round(self.y, 9)))
    
    def __repr__(self):
        return f"({self.x}, {self.y})"

def cross(o, a, b):
    return (a.x - o.x) * (b.y - o.y) - (a.y - o.y) * (b.x - o.x)

def distance_sq(a, b):
    return (a.x - b.x)**2 + (a.y - b.y)**2

def circumcenter(a, b, c):
    """Calculate circumcenter of triangle abc"""
    d = 2 * (a.x * (b.y - c.y) + b.x * (c.y - a.y) + c.x * (a.y - b.y))
    
    if abs(d) < 1e-9:
        return None  # Points are colinear
    
    ux = ((a.x*a.x + a.y*a.y) * (b.y - c.y) + 
          (b.x*b.x + b.y*b.y) * (c.y - a.y) + 
          (c.x*c.x + c.y*c.y) * (a.y - b.y)) / d
    
    uy = ((a.x*a.x + a.y*a.y) * (c.x - b.x) + 
          (b.x*b.x + b.y*b.y) * (a.x - c.x) + 
          (c.x*c.x + c.y*c.y) * (b.x - a.x)) / d
    
    return Point(ux, uy)

def line_intersection(a1, a2, b1, b2):
    """Find intersection point of two lines"""
    A1 = a2.y - a1.y
    B1 = a1.x - a2.x
    C1 = A1 * a1.x + B1 * a1.y
    
    A2 = b2.y - b1.y
    B2 = b1.x - b2.x
    C2 = A2 * b1.x + B2 * b1.y
    
    determinant = A1 * B2 - A2 * B1
    
    if abs(determinant) < 1e-9:
        return None  # Lines are parallel
    
    x = (B2 * C1 - B1 * C2) / determinant
    y = (A1 * C2 - A2 * C1) / determinant
    
    return Point(x, y)

class BoundedVoronoi:
    def __init__(self, sites):
        self.sites = sites
        self.n = len(sites)
        
        # Calculate bounding box with padding
        if sites:
            xs = [p.x for p in sites]
            ys = [p.y for p in sites]
            self.min_x = min(xs) - 10
            self.max_x = max(xs) + 10
            self.min_y = min(ys) - 10
            self.max_y = max(ys) + 10
        else:
            self.min_x = self.min_y = -10
            self.max_x = self.max_y = 10
    
    def delaunay_triangulation(self):
        """Compute Delaunay triangulation"""
        triangles = []
        
        for i in range(self.n):
            for j in range(i + 1, self.n):
                for k in range(j + 1, self.n):
                    a, b, c = self.sites[i], self.sites[j], self.sites[k]
                    
                    if abs(cross(a, b, c)) < 1e-9:
                        continue
                    
                    is_delaunay = True
                    for l in range(self.n):
                        if l != i and l != j and l != k:
                            if self.in_circumcircle(a, b, c, self.sites[l]):
                                is_delaunay = False
                                break
                    
                    if is_delaunay:
                        triangles.append((i, j, k))
        
        return triangles
    
    def in_circumcircle(self, a, b, c, p):
        """Check if point p is inside circumcircle of triangle abc"""
        d11 = a.x - p.x
        d12 = a.y - p.y
        d21 = b.x - p.x
        d22 = b.y - p.y
        d31 = c.x - p.x
        d32 = c.y - p.y
        
        det = (d11 * d11 + d12 * d12) * (d21 * d32 - d22 * d31) - \
              (d21 * d21 + d22 * d22) * (d11 * d32 - d12 * d31) + \
              (d31 * d31 + d32 * d32) * (d11 * d22 - d12 * d21)
        
        return det > 1e-9
    
    def compute_bounded_voronoi(self):
        """Compute Voronoi diagram clipped to bounding box"""
        triangles = self.delaunay_triangulation()
        
        # Calculate circumcenters
        voronoi_vertices = []
        triangle_to_vertex = {}
        
        for triangle in triangles:
            a, b, c = [self.sites[i] for i in triangle]
            center = circumcenter(a, b, c)
            if center:
                # Clip to bounding box
                center.x = max(self.min_x, min(self.max_x, center.x))
                center.y = max(self.min_y, min(self.max_y, center.y))
                
                found = False
                for idx, vertex in enumerate(voronoi_vertices):
                    if abs(vertex.x - center.x) < 1e-9 and abs(vertex.y - center.y) < 1e-9:
                        triangle_to_vertex[triangle] = idx
                        found = True
                        break
                
                if not found:
                    triangle_to_vertex[triangle] = len(voronoi_vertices)
                    voronoi_vertices.append(center)
        
        # Add bounding box corners as additional vertices for clipped regions
        bbox_vertices = [
            Point(self.min_x, self.min_y),
            Point(self.max_x, self.min_y),
            Point(self.max_x, self.max_y),
            Point(self.min_x, self.max_y)
        ]
        
        bbox_start_idx = len(voronoi_vertices)
        voronoi_vertices.extend(bbox_vertices)
        
        # Create edges between adjacent triangles
        voronoi_edges = set()
        
        # Map edges to triangles
        edge_to_triangles = {}
        for triangle in triangles:
            i, j, k = triangle
            edges = [(min(i,j), max(i,j)), 
                    (min(j,k), max(j,k)), 
                    (min(k,i), max(k,i))]
            for edge in edges:
                if edge not in edge_to_triangles:
                    edge_to_triangles[edge] = []
                edge_to_triangles[edge].append(triangle)
        
        # Connect Voronoi vertices of adjacent triangles
        for edge, adjacent_triangles in edge_to_triangles.items():
            if len(adjacent_triangles) == 2:
                tri1, tri2 = adjacent_triangles
                if tri1 in triangle_to_vertex and tri2 in triangle_to_vertex:
                    v1 = triangle_to_vertex[tri1]
                    v2 = triangle_to_vertex[tri2]
                    if v1 != v2:
                        voronoi_edges.add((min(v1, v2), max(v1, v2)))
        
        # For triangles on convex hull, connect to bounding box
        # This is a simplified approach - full implementation would be more complex
        hull_edges = set()
        for i in range(4):
            hull_edges.add((bbox_start_idx + i, bbox_start_idx + (i + 1) % 4))
        
        # Add some connections from Voronoi vertices to bounding box
        # (This is a simplified version - real implementation would use proper clipping)
        if voronoi_vertices:
            center_idx = 0  # Use first vertex as representative
            for i in range(4):
                voronoi_edges.add((center_idx, bbox_start_idx + i))
        
        return voronoi_vertices, list(voronoi_edges.union(hull_edges))

def solve_bounded_voronoi():
    import sys
    input = sys.stdin.read().split()
    idx = 0
    
    # Read sites
    n = int(input[idx]); idx += 1
    sites = []
    for _ in range(n):
        x = float(input[idx]); y = float(input[idx+1]); idx += 2
        sites.append(Point(x, y))
    
    # Compute bounded Voronoi diagram
    voronoi = BoundedVoronoi(sites)
    vertices, edges = voronoi.compute_bounded_voronoi()
    
    # Output results
    results = [str(len(vertices))]
    for vertex in vertices:
        results.append(f"{vertex.x:.2f} {vertex.y:.2f}")
    
    results.append(str(len(edges)))
    for edge in sorted(edges):
        results.append(f"{edge[0]} {edge[1]}")
    
    return results