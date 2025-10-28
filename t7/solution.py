import sys
import bisect

def find_lis(arr):
    n = len(arr)
    if n == 0:
        return 0, []
    
    # For storing the smallest tail of all increasing subsequences
    tail = []
    # For storing predecessors to reconstruct the sequence
    prev = [-1] * n
    # For storing indices of elements in tail array
    indices = []
    
    for i in range(n):
        # Find the position where arr[i] should be inserted
        pos = bisect.bisect_left(tail, arr[i])
        
        if pos == len(tail):
            # If arr[i] is larger than all tails, extend the LIS
            tail.append(arr[i])
            indices.append(i)
        else:
            # Replace the tail at this position
            tail[pos] = arr[i]
            indices[pos] = i
        
        # Store predecessor for reconstruction
        if pos > 0:
            prev[i] = indices[pos - 1]
    
    # Reconstruct the LIS
    lis_length = len(tail)
    lis_seq = []
    
    # Start from the last element in the LIS
    current = indices[-1]
    for _ in range(lis_length):
        lis_seq.append(arr[current])
        current = prev[current]
        if current == -1:
            break
    
    lis_seq.reverse()
    return lis_length, lis_seq

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    arr = list(map(int, data[1:1+n]))
    
    lis_length, lis_seq = find_lis(arr)
    
    print(f"LIS length: {lis_length}")
    print(f"One LIS: {' '.join(map(str, lis_seq))}")

if __name__ == "__main__":
    main()