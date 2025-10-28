import sys
import math
import random
import numpy as np
from collections import deque

class AntColonyOptimization:
    def __init__(self, grid, num_ants, num_iterations, evaporation_rate, 
                 alpha=1.0, beta=2.0, q0=0.9):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.num_ants = num_ants
        self.num_iterations = num_iterations
        self.evaporation_rate = evaporation_rate
        self.alpha = alpha  # Pheromone importance
        self.beta = beta    # Heuristic importance
        self.q0 = q0        # Exploitation probability
        
        # Find start and end positions
        self.start_pos = None
        self.end_pos = None
        self.find_start_end()
        
        # Initialize pheromone matrix
        self.pheromone = np.ones((self.rows, self.cols)) * 0.1
        
        # Best path found
        self.best_path = None
        self.best_path_length = float('inf')
        
    def find_start_end(self):
        """Find start (S) and end (E) positions in grid"""
        for i in range(self.rows):
            for j in range(self.cols):
                if self.grid[i][j] == 'S':
                    self.start_pos = (i, j)
                elif self.grid[i][j] == 'E':
                    self.end_pos = (i, j)
        
        if self.start_pos is None or self.end_pos is None:
            raise ValueError("Start (S) or End (E) position not found in grid")
    
    def is_valid_position(self, pos):
        """Check if position is within grid and not obstacle"""
        i, j = pos
        return (0 <= i < self.rows and 0 <= j < self.cols and 
                self.grid[i][j] != '#')
    
    def get_neighbors(self, pos):
        """Get valid neighboring positions (up, down, left, right)"""
        i, j = pos
        neighbors = []
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
        
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if self.is_valid_position((ni, nj)):
                neighbors.append((ni, nj))
        
        return neighbors
    
    def manhattan_distance(self, pos1, pos2):
        """Calculate Manhattan distance between two positions"""
        return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])
    
    def heuristic_value(self, pos):
        """Heuristic value based on distance to target"""
        return 1.0 / (1.0 + self.manhattan_distance(pos, self.end_pos))
    
    def choose_next_position(self, current_pos, visited):
        """Choose next position based on pheromone and heuristic"""
        neighbors = self.get_neighbors(current_pos)
        
        # Remove visited positions
        unvisited_neighbors = [n for n in neighbors if n not in visited]
        
        if not unvisited_neighbors:
            return None
        
        # Calculate probabilities for each neighbor
        probabilities = []
        total = 0.0
        
        for neighbor in unvisited_neighbors:
            i, j = neighbor
            pheromone_val = self.pheromone[i][j]
            heuristic_val = self.heuristic_value(neighbor)
            
            # Probability based on pheromone and heuristic
            probability = (pheromone_val ** self.alpha) * (heuristic_val ** self.beta)
            probabilities.append(probability)
            total += probability
        
        if total == 0:
            # If all probabilities are zero, choose randomly
            return random.choice(unvisited_neighbors)
        
        # Normalize probabilities
        probabilities = [p / total for p in probabilities]
        
        # Exploitation vs Exploration
        if random.random() < self.q0:
            # Exploitation: choose best
            best_idx = np.argmax(probabilities)
            return unvisited_neighbors[best_idx]
        else:
            # Exploration: choose probabilistically
            # Use random.choices instead of np.random.choice for 2D positions
            return random.choices(unvisited_neighbors, weights=probabilities)[0]
    
    def construct_ant_path(self):
        """Construct path for one ant"""
        current_pos = self.start_pos
        path = [current_pos]
        visited = set([current_pos])
        
        max_steps = self.rows * self.cols  # Prevent infinite loops
        
        for step in range(max_steps):
            if current_pos == self.end_pos:
                break
                
            next_pos = self.choose_next_position(current_pos, visited)
            
            if next_pos is None:
                # Dead end
                return None
            
            path.append(next_pos)
            visited.add(next_pos)
            current_pos = next_pos
        
        if path[-1] != self.end_pos:
            return None  # Failed to reach target
        
        return path
    
    def update_pheromone(self, paths):
        """Update pheromone trails with evaporation and ant deposits"""
        # Evaporation
        self.pheromone *= (1.0 - self.evaporation_rate)
        
        # Add pheromone from ant paths
        for path in paths:
            if path is None:
                continue
                
            path_length = len(path)
            if path_length > 0:
                # Pheromone deposit is inversely proportional to path length
                pheromone_deposit = 1.0 / path_length
                
                for pos in path:
                    i, j = pos
                    self.pheromone[i][j] += pheromone_deposit
    
    def find_shortest_path_bfs(self):
        """Find shortest path using BFS for comparison"""
        queue = deque([(self.start_pos, [self.start_pos])])
        visited = set([self.start_pos])
        
        while queue:
            current_pos, path = queue.popleft()
            
            if current_pos == self.end_pos:
                return path
            
            for neighbor in self.get_neighbors(current_pos):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, path + [neighbor]))
        
        return None
    
    def run(self):
        """Run Ant Colony Optimization"""
        for iteration in range(self.num_iterations):
            ant_paths = []
            
            # Let each ant construct a path
            for ant in range(self.num_ants):
                path = self.construct_ant_path()
                ant_paths.append(path)
                
                # Update best path
                if path and len(path) < self.best_path_length:
                    self.best_path = path
                    self.best_path_length = len(path)
            
            # Update pheromone trails
            self.update_pheromone(ant_paths)
            
            # Early stopping if optimal path found
            if self.best_path_length == self.manhattan_distance(self.start_pos, self.end_pos) + 1:
                break
        
        return self.best_path, self.best_path_length

def solve_ant_colony():
    input_lines = sys.stdin.read().splitlines()
    if not input_lines:
        return []
    
    # Parse grid size
    n, m = map(int, input_lines[0].split())
    
    # Parse grid
    grid = []
    for i in range(1, 1 + n):
        grid.append(list(input_lines[i].strip()))
    
    # Parse ACO parameters
    params = input_lines[1 + n].split()
    num_ants = int(params[0])
    num_iterations = int(params[1])
    evaporation_rate = float(params[2])
    
    # Set random seed for reproducibility
    random.seed(42)
    np.random.seed(42)
    
    # Run Ant Colony Optimization
    aco = AntColonyOptimization(grid, num_ants, num_iterations, evaporation_rate)
    best_path, path_length = aco.run()
    
    # If ACO failed, use BFS as fallback
    if best_path is None:
        best_path = aco.find_shortest_path_bfs()
        if best_path:
            path_length = len(best_path)
        else:
            path_length = -1
    
    # Format output
    results = []
    if best_path:
        results.append(str(path_length))
        path_str = " ".join(f"{r},{c}" for r, c in best_path)
        results.append(path_str)
    else:
        results.append("-1")
        results.append("No path found")
    
    return results