import sys
import math
from functools import lru_cache

class GrundyCalculator:
    def __init__(self):
        self.max_n = 10**6
        self.power_precompute()
        self.divide_precompute()
    
    def power_precompute(self):
        """Precompute Grundy numbers for power game"""
        squares = []
        i = 1
        while i * i <= self.max_n:
            squares.append(i * i)
            i += 1
        
        self.power_grundy = [0] * (self.max_n + 1)
        for n in range(1, self.max_n + 1):
            reachable = set()
            for sq in squares:
                if sq > n:
                    break
                reachable.add(self.power_grundy[n - sq])
            
            g = 0
            while g in reachable:
                g += 1
            self.power_grundy[n] = g
    
    def divide_precompute(self):
        """Precompute Grundy numbers for division game"""
        self.divide_grundy = [0] * (self.max_n + 1)
        for n in range(1, self.max_n + 1):
            reachable = set()
            # Move to floor(n/2)
            reachable.add(self.divide_grundy[n // 2])
            # Move to floor(n/3)  
            reachable.add(self.divide_grundy[n // 3])
            
            g = 0
            while g in reachable:
                g += 1
            self.divide_grundy[n] = g
    
    def take_away_grundy(self, n):
        """Grundy number for take-away game (remove 1,2,3 stones)"""
        return n % 4
    
    def power_game_grundy(self, n):
        return self.power_grundy[n]
    
    def division_game_grundy(self, n):
        return self.divide_grundy[n]

def solve_grundy_game():
    input = sys.stdin.read().split()
    idx = 0
    T = int(input[idx]); idx += 1
    
    calculator = GrundyCalculator()
    results = []
    
    for _ in range(T):
        G = int(input[idx]); idx += 1
        total_xor = 0
        
        for _ in range(G):
            game_type = input[idx]; idx += 1
            n = int(input[idx]); idx += 1
            
            if game_type == "take":
                grundy = calculator.take_away_grundy(n)
            elif game_type == "power":
                grundy = calculator.power_game_grundy(n)
            elif game_type == "divide":
                grundy = calculator.division_game_grundy(n)
            
            total_xor ^= grundy
        
        if total_xor != 0:
            results.append("First")
        else:
            results.append("Second")
    
    return results