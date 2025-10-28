import sys
import math
import random
import numpy as np

def rastrigin_function(x, A=10):
    """
    Rastrigin function: f(x) = A*n + Σ[x_i² - A*cos(2πx_i)]
    Global minimum: f(0,0,...,0) = 0
    """
    n = len(x)
    sum_val = A * n
    for i in range(n):
        sum_val += x[i]**2 - A * math.cos(2 * math.pi * x[i])
    return sum_val

class ParticleSwarmOptimization:
    def __init__(self, dimensions, num_particles, max_iterations, w, c1, c2):
        self.dimensions = dimensions
        self.num_particles = num_particles
        self.max_iterations = max_iterations
        self.w = w  # Inertia weight
        self.c1 = c1  # Cognitive parameter
        self.c2 = c2  # Social parameter
        
        # Search space bounds
        self.min_bound = -5.12
        self.max_bound = 5.12
        
        # Initialize particles
        self.positions = np.random.uniform(
            self.min_bound, self.max_bound, (num_particles, dimensions)
        )
        self.velocities = np.random.uniform(
            -1, 1, (num_particles, dimensions)
        )
        
        # Initialize personal bests
        self.pbest_positions = self.positions.copy()
        self.pbest_fitness = np.array([rastrigin_function(pos) for pos in self.positions])
        
        # Initialize global best
        self.gbest_index = np.argmin(self.pbest_fitness)
        self.gbest_position = self.pbest_positions[self.gbest_index].copy()
        self.gbest_fitness = self.pbest_fitness[self.gbest_index]
        
        # Convergence tracking
        self.convergence_data = []
    
    def update_velocity(self, velocity, position, pbest, gbest):
        """Update particle velocity"""
        r1 = np.random.random(self.dimensions)
        r2 = np.random.random(self.dimensions)
        
        cognitive = self.c1 * r1 * (pbest - position)
        social = self.c2 * r2 * (gbest - position)
        
        new_velocity = self.w * velocity + cognitive + social
        
        # Velocity clamping to prevent explosion
        max_velocity = 0.2 * (self.max_bound - self.min_bound)
        new_velocity = np.clip(new_velocity, -max_velocity, max_velocity)
        
        return new_velocity
    
    def update_position(self, position, velocity):
        """Update particle position"""
        new_position = position + velocity
        
        # Position clamping to stay in search space
        new_position = np.clip(new_position, self.min_bound, self.max_bound)
        
        return new_position
    
    def optimize(self):
        """Run PSO optimization"""
        for iteration in range(self.max_iterations):
            for i in range(self.num_particles):
                # Update velocity and position
                self.velocities[i] = self.update_velocity(
                    self.velocities[i],
                    self.positions[i],
                    self.pbest_positions[i],
                    self.gbest_position
                )
                
                self.positions[i] = self.update_position(
                    self.positions[i],
                    self.velocities[i]
                )
                
                # Evaluate fitness
                current_fitness = rastrigin_function(self.positions[i])
                
                # Update personal best
                if current_fitness < self.pbest_fitness[i]:
                    self.pbest_positions[i] = self.positions[i].copy()
                    self.pbest_fitness[i] = current_fitness
                    
                    # Update global best
                    if current_fitness < self.gbest_fitness:
                        self.gbest_position = self.positions[i].copy()
                        self.gbest_fitness = current_fitness
            
            # Record convergence
            self.convergence_data.append(self.gbest_fitness)
            
            # Early stopping if converged
            if (iteration > 50 and 
                abs(self.convergence_data[-1] - self.convergence_data[-50]) < 1e-10):
                break
        
        return self.gbest_position, self.gbest_fitness, self.convergence_data
    
    def get_results(self):
        """Get formatted results"""
        best_position_str = ",".join(f"{x:.6f}" for x in self.gbest_position)
        best_fitness_str = f"{self.gbest_fitness:.6f}"
        
        # Sample convergence data
        if len(self.convergence_data) <= 10:
            convergence_str = ",".join(f"{x:.3f}" for x in self.convergence_data)
        else:
            # Take first 5, last 5, and some middle values
            sampled_data = (
                self.convergence_data[:5] + 
                self.convergence_data[-5:] +
                self.convergence_data[len(self.convergence_data)//2-2:len(self.convergence_data)//2+3]
            )
            convergence_str = ",".join(f"{x:.3f}" for x in sampled_data)
        
        return best_position_str, best_fitness_str, convergence_str

def solve_pso():
    input = sys.stdin.read().split()
    if not input:
        return []
    
    dimensions = int(input[0])
    num_particles = int(input[1])
    max_iterations = int(input[2])
    w = float(input[3])
    c1 = float(input[4])
    c2 = float(input[5])
    
    # Set random seed for reproducibility
    random.seed(42)
    np.random.seed(42)
    
    # Run PSO
    pso = ParticleSwarmOptimization(dimensions, num_particles, max_iterations, w, c1, c2)
    pso.optimize()
    
    best_position, best_fitness, convergence_data = pso.get_results()
    
    # Format output
    results = []
    results.append(best_position)
    results.append(best_fitness)
    results.append(convergence_data)
    
    return results

if __name__ == "__main__":
    results = solve_pso()
    for result in results:
        print(result)