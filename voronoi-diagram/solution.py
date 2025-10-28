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
    
    def __repr__(self):
        return f"({self.x}, {self.y})"

def distance_sq(a, b):
    return (a.x - b.x)**2 + (a.y - b.y)**2

class VoronoiDiagram:
    def __init__(self, sites):
        self.sites = sites
        self.n = len(sites)
    
    def find_closest_site(self, query_point):
        """Find the closest site to query point using brute force for simplicity"""
        min_dist = float('inf')
        closest_site = 0
        
        for i, site in enumerate(self.sites):
            dist = distance_sq(site, query_point)
            if dist < min_dist:
                min_dist = dist
                closest_site = i
            elif abs(dist - min_dist) < 1e-9:
                # If equal distance, choose smaller index
                if i < closest_site:
                    closest_site = i
        
        return closest_site

def solve_voronoi():
    import sys
    input = sys.stdin.read().split()
    idx = 0
    
    # Read sites
    n = int(input[idx]); idx += 1
    sites = []
    for _ in range(n):
        x = float(input[idx]); y = float(input[idx+1]); idx += 2
        sites.append(Point(x, y))
    
    # Create Voronoi diagram
    voronoi = VoronoiDiagram(sites)
    
    # Read queries
    q = int(input[idx]); idx += 1
    results = []
    
    for _ in range(q):
        x = float(input[idx]); y = float(input[idx+1]); idx += 2
        query_point = Point(x, y)
        closest = voronoi.find_closest_site(query_point)
        results.append(str(closest))
    
    return results

if __name__ == '__main__':
    results = solve_voronoi()
    for result in results:
        print(result)