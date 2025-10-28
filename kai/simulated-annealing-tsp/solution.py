import sys
import math
import random
import numpy as np

def euclidean_distance(p1, p2):
    """Calculate Euclidean distance between two points"""
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def total_distance(tour, distances):
    """Calculate total distance of a tour"""
    total = 0
    n = len(tour)
    for i in range(n):
        total += distances[tour[i]][tour[(i + 1) % n]]
    return total

def create_distance_matrix(cities):
    """Create distance matrix between all cities"""
    n = len(cities)
    distances = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            dist = euclidean_distance(cities[i], cities[j])
            distances[i][j] = dist
            distances[j][i] = dist
    return distances

def initial_solution(n):
    """Create initial random solution"""
    tour = list(range(n))
    random.shuffle(tour)
    return tour

def two_opt_swap(tour, i, k):
    """Perform 2-opt swap on tour"""
    new_tour = tour[:i] + tour[i:k+1][::-1] + tour[k+1:]
    return new_tour

def simulated_annealing_tsp(cities, initial_temp=10000, cooling_rate=0.9995, max_iter=100000):
    """Solve TSP using Simulated Annealing"""
    n = len(cities)
    distances = create_distance_matrix(cities)
    
    # Initial solution
    current_tour = initial_solution(n)
    current_distance = total_distance(current_tour, distances)
    
    best_tour = current_tour[:]
    best_distance = current_distance
    
    temperature = initial_temp
    
    for iteration in range(max_iter):
        # Generate neighbor using 2-opt
        i = random.randint(0, n - 2)
        k = random.randint(i + 1, n - 1)
        
        new_tour = two_opt_swap(current_tour, i, k)
        new_distance = total_distance(new_tour, distances)
        
        # Calculate energy difference
        delta = new_distance - current_distance
        
        # Acceptance criteria
        if delta < 0 or random.random() < math.exp(-delta / temperature):
            current_tour = new_tour
            current_distance = new_distance
            
            # Update best solution
            if current_distance < best_distance:
                best_tour = current_tour[:]
                best_distance = current_distance
        
        # Cool down
        temperature *= cooling_rate
        
        # Early stopping if temperature is very low
        if temperature < 1e-8:
            break
    
    return best_tour, best_distance

def solve_tsp():
    input = sys.stdin.read().splitlines()
    if not input:
        return []
    
    n = int(input[0])
    cities = []
    for i in range(1, 1 + n):
        x, y = map(float, input[i].split())
        cities.append((x, y))
    
    # Set random seed for reproducibility
    random.seed(42)
    np.random.seed(42)
    
    # Run simulated annealing
    best_tour, best_distance = simulated_annealing_tsp(cities)
    
    # Format output
    results = []
    results.append(f"{best_distance:.6f}")
    results.append(" ".join(map(str, best_tour)))
    
    return results