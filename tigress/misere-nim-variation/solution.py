import sys

def calculate_grundy(pile_type, size):
    """
    Calculate Grundy number for a pile based on type and size
    """
    if pile_type == "normal":
        # For normal piles in misère Nim:
        # Grundy = size, except special handling for all piles of size 1
        return size
    elif pile_type == "special":
        # For special piles (can only remove 1,2,3):
        # Grundy number cycles with period 4
        return size % 4
    return 0

def solve_misere_nim():
    input = sys.stdin.read().split()
    idx = 0
    T = int(input[idx]); idx += 1
    results = []
    
    for _ in range(T):
        N = int(input[idx]); idx += 1
        
        piles = []
        all_normal = True
        all_size_one = True
        has_large_pile = False
        
        for _ in range(N):
            pile_type = input[idx]; idx += 1
            size = int(input[idx]); idx += 1
            piles.append((pile_type, size))
            
            if pile_type != "normal":
                all_normal = False
            if size > 1:
                all_size_one = False
            if size > 1:
                has_large_pile = True
        
        # Special case: All piles are normal and all have size 1
        if all_normal and all_size_one:
            # In misère Nim with all piles size 1:
            # If odd number of piles: First loses (must take last stone)
            # If even number of piles: First wins (opponent takes last stone)
            if N % 2 == 1:
                results.append("Second")
            else:
                results.append("First")
            continue
        
        # Special case: All piles are special and all have size 1
        if all(pile_type == "special" for pile_type, size in piles) and all_size_one:
            # All special piles of size 1: player must take last stone and lose
            if N % 2 == 1:
                results.append("Second")
            else:
                results.append("First")
            continue
        
        # General case: Calculate XOR of Grundy numbers
        xor_sum = 0
        for pile_type, size in piles:
            grundy = calculate_grundy(pile_type, size)
            xor_sum ^= grundy
        
        # In misère Nim with mixed piles, use normal winning condition
        # XOR != 0 means first player wins
        if xor_sum != 0:
            results.append("First")
        else:
            results.append("Second")
    
    return results

if __name__ == "__main__":
    results = solve_misere_nim()
    for result in results:
        print(result)