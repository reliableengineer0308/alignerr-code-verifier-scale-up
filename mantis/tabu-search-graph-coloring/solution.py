import sys
import random
import numpy as np
from collections import deque, defaultdict

class TabuSearchGraphColoring:
    def __init__(self, graph, num_vertices, tabu_size, max_iterations):
        self.graph = graph
        self.num_vertices = num_vertices
        self.tabu_size = tabu_size
        self.max_iterations = max_iterations
        
        # Initialize coloring
        self.colors = None
        self.num_colors = 0
        
        # Tabu list: (vertex, color) -> remaining iterations
        self.tabu_list = {}
        
        # Best solution found
        self.best_coloring = None
        self.best_num_colors = float('inf')
        self.best_conflicts = float('inf')
        
    def initialize_coloring(self, initial_colors):
        """Initialize with given number of colors"""
        self.num_colors = initial_colors
        self.colors = [random.randint(0, self.num_colors - 1) for _ in range(self.num_vertices)]
        
    def count_conflicts(self):
        """Count number of conflicting edges"""
        conflicts = 0
        for u in range(self.num_vertices):
            for v in self.graph[u]:
                if v > u and self.colors[u] == self.colors[v]:
                    conflicts += 1
        return conflicts
    
    def is_valid_coloring(self):
        """Check if current coloring is valid (no conflicts)"""
        return self.count_conflicts() == 0
    
    def get_neighbors(self):
        """Generate neighborhood by changing one vertex's color"""
        neighbors = []
        current_conflicts = self.count_conflicts()
        
        # Find conflicting vertices
        conflicting_vertices = set()
        for u in range(self.num_vertices):
            for v in self.graph[u]:
                if self.colors[u] == self.colors[v]:
                    conflicting_vertices.add(u)
                    conflicting_vertices.add(v)
        
        # If no conflicts, try to reduce number of colors
        if not conflicting_vertices:
            # Try to remove one color
            color_usage = defaultdict(set)
            for v, color in enumerate(self.colors):
                color_usage[color].add(v)
            
            # Find least used color
            least_used_color = min(color_usage.keys(), key=lambda c: len(color_usage[c]))
            
            # Recolor vertices using the least used color
            for v in color_usage[least_used_color]:
                for new_color in range(self.num_colors):
                    if new_color != least_used_color:
                        # Check if move is tabu
                        if (v, new_color) in self.tabu_list:
                            continue
                        
                        neighbor = self.colors.copy()
                        neighbor[v] = new_color
                        neighbors.append((neighbor, v, new_color))
            
            return neighbors
        
        # Generate moves for conflicting vertices
        for v in conflicting_vertices:
            current_color = self.colors[v]
            for new_color in range(self.num_colors):
                if new_color != current_color:
                    # Check if move is tabu
                    if (v, new_color) in self.tabu_list:
                        continue
                    
                    neighbor = self.colors.copy()
                    neighbor[v] = new_color
                    neighbors.append((neighbor, v, new_color))
        
        return neighbors
    
    def evaluate_coloring(self, coloring):
        """Evaluate a coloring (lower is better)"""
        conflicts = 0
        for u in range(self.num_vertices):
            for v in self.graph[u]:
                if v > u and coloring[u] == coloring[v]:
                    conflicts += 1
        return conflicts
    
    def update_tabu_list(self):
        """Update tabu list - decrease counters and remove expired entries"""
        expired_entries = []
        for key, count in self.tabu_list.items():
            if count <= 1:
                expired_entries.append(key)
            else:
                self.tabu_list[key] = count - 1
        
        for key in expired_entries:
            del self.tabu_list[key]
    
    def add_to_tabu_list(self, vertex, color, tenure=None):
        """Add move to tabu list"""
        if tenure is None:
            tenure = random.randint(5, 15)  # Dynamic tabu tenure
        
        self.tabu_list[(vertex, color)] = tenure
        
        # Maintain tabu list size
        if len(self.tabu_list) > self.tabu_size:
            # Remove oldest entry (not exactly FIFO but good enough)
            oldest_key = next(iter(self.tabu_list))
            del self.tabu_list[oldest_key]
    
    def search(self):
        """Run Tabu Search for graph coloring"""
        # Start with upper bound (greedy coloring estimate)
        upper_bound = self.estimate_upper_bound()
        current_num_colors = upper_bound
        
        while current_num_colors >= 1:
            print(f"Trying with {current_num_colors} colors...", file=sys.stderr)
            
            # Initialize coloring with current number of colors
            self.initialize_coloring(current_num_colors)
            current_conflicts = self.count_conflicts()
            
            # Local search with current number of colors
            for iteration in range(self.max_iterations):
                self.update_tabu_list()
                
                # Generate neighborhood
                neighbors = self.get_neighbors()
                
                if not neighbors:
                    break
                
                # Evaluate neighbors
                best_neighbor = None
                best_conflicts = float('inf')
                best_move = None
                
                for neighbor, vertex, new_color in neighbors:
                    conflicts = self.evaluate_coloring(neighbor)
                    
                    # Aspiration criteria: accept if better than global best
                    aspiration = (conflicts == 0 and current_num_colors <= self.best_num_colors)
                    
                    if conflicts < best_conflicts or aspiration:
                        best_neighbor = neighbor
                        best_conflicts = conflicts
                        best_move = (vertex, new_color)
                
                if best_neighbor is None:
                    break
                
                # Apply best move
                self.colors = best_neighbor
                current_conflicts = best_conflicts
                
                # Add to tabu list
                if best_move:
                    vertex, new_color = best_move
                    self.add_to_tabu_list(vertex, new_color)
                
                # Update best solution
                if current_conflicts == 0 and current_num_colors < self.best_num_colors:
                    self.best_coloring = self.colors.copy()
                    self.best_num_colors = current_num_colors
                    self.best_conflicts = 0
                
                # Early stopping if valid coloring found
                if current_conflicts == 0:
                    break
            
            # If we found a valid coloring with current_num_colors, try with fewer colors
            if current_conflicts == 0:
                current_num_colors -= 1
            else:
                # If no valid coloring found, stop
                break
        
        return self.best_coloring, self.best_num_colors
    
    def estimate_upper_bound(self):
        """Estimate upper bound for number of colors using greedy algorithm"""
        colors = [-1] * self.num_vertices
        colors[0] = 0
        
        available = [True] * self.num_vertices
        
        for u in range(1, self.num_vertices):
            # Reset available colors
            for i in range(self.num_vertices):
                available[i] = True
            
            # Mark colors of adjacent vertices as unavailable
            for v in self.graph[u]:
                if colors[v] != -1:
                    available[colors[v]] = False
            
            # Find first available color
            color = 0
            while color < self.num_vertices:
                if available[color]:
                    break
                color += 1
            
            colors[u] = color
        
        return max(colors) + 1

def solve_graph_coloring():
    input_lines = sys.stdin.read().splitlines()
    if not input_lines:
        return []
    
    # Parse graph
    n, m = map(int, input_lines[0].split())
    
    # Build adjacency list
    graph = [[] for _ in range(n)]
    for i in range(1, 1 + m):
        u, v = map(int, input_lines[i].split())
        graph[u].append(v)
        graph[v].append(u)
    
    # Parse Tabu Search parameters
    params = input_lines[1 + m].split()
    tabu_size = int(params[0])
    max_iterations = int(params[1])
    
    # Set random seed for reproducibility
    random.seed(42)
    np.random.seed(42)
    
    # Run Tabu Search
    ts = TabuSearchGraphColoring(graph, n, tabu_size, max_iterations)
    best_coloring, num_colors = ts.search()
    
    # If no valid coloring found, use the best attempt
    if best_coloring is None:
        best_coloring = ts.colors
        num_colors = max(best_coloring) + 1 if best_coloring else 0
    
    # Format output
    results = []
    results.append(str(num_colors))
    if best_coloring:
        results.append(" ".join(map(str, best_coloring)))
    else:
        results.append("")
    
    return results