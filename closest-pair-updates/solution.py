import math
import bisect
from sortedcontainers import SortedList

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __hash__(self):
        return hash((self.x, self.y))
    
    def __repr__(self):
        return f"({self.x}, {self.y})"

class ClosestPairMaintainer:
    def __init__(self):
        self.points = set()
        self.points_list = SortedList(key=lambda p: (p.x, p.y))
        self.min_distance_sq = float('inf')
    
    def distance_sq(self, p1, p2):
        return (p1.x - p2.x)**2 + (p1.y - p2.y)**2
    
    def add_point(self, x, y):
        new_point = Point(x, y)
        if new_point in self.points:
            return
        
        self.points.add(new_point)
        
        # Find position to insert
        idx = self.points_list.bisect_left(new_point)
        self.points_list.add(new_point)
        
        # Check neighbors for new minimum
        for i in range(max(0, idx - 5), min(len(self.points_list), idx + 6)):
            if self.points_list[i] != new_point:
                dist_sq = self.distance_sq(new_point, self.points_list[i])
                if dist_sq < self.min_distance_sq:
                    self.min_distance_sq = dist_sq
    
    def remove_point(self, x, y):
        point_to_remove = Point(x, y)
        if point_to_remove not in self.points:
            return
        
        self.points.remove(point_to_remove)
        self.points_list.remove(point_to_remove)
        
        # If we have less than 2 points, reset min distance
        if len(self.points) < 2:
            self.min_distance_sq = float('inf')
            return
        
        # Recompute min distance if we removed a point that was part of closest pair
        self.min_distance_sq = float('inf')
        points_sorted = sorted(self.points_list, key=lambda p: (p.x, p.y))
        
        for i in range(len(points_sorted)):
            for j in range(i + 1, min(i + 8, len(points_sorted))):
                dist_sq = self.distance_sq(points_sorted[i], points_sorted[j])
                if dist_sq < self.min_distance_sq:
                    self.min_distance_sq = dist_sq
    
    def query(self):
        if len(self.points) < 2:
            return 0
        return int(self.min_distance_sq)

def solve_closest_pair():
    import sys
    input = sys.stdin.read().splitlines()
    Q = int(input[0])
    maintainer = ClosestPairMaintainer()
    results = []
    
    for i in range(1, Q + 1):
        parts = input[i].split()
        if parts[0] == "ADD":
            x, y = int(parts[1]), int(parts[2])
            maintainer.add_point(x, y)
        elif parts[0] == "REMOVE":
            x, y = int(parts[1]), int(parts[2])
            maintainer.remove_point(x, y)
        elif parts[0] == "QUERY":
            results.append(str(maintainer.query()))
    
    return results