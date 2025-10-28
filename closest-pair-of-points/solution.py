import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def brute_force(points):
    min_dist = float('inf')
    pair = None
    n = len(points)
    for i in range(n):
        for j in range(i + 1, n):
            dist = euclidean_distance(points[i], points[j])
            if dist < min_dist:
                min_dist = dist
                pair = (points[i], points[j])
    return min_dist, pair

def closest_pair_rec(px, py):
    if len(px) <= 3:
        return brute_force(px)
    
    mid = len(px) // 2
    midpoint = px[mid]
    
    q_x = px[:mid]
    r_x = px[mid:]
    
    q_y = list(filter(lambda x: x[0] <= midpoint[0], py))
    r_y = list(filter(lambda x: x[0] > midpoint[0], py))
    
    dl, pair_l = closest_pair_rec(q_x, q_y)
    dr, pair_r = closest_pair_rec(r_x, r_y)
    
    if dl <= dr:
        d = dl
        min_pair = pair_l
    else:
        d = dr
        min_pair = pair_r
    
    strip = [p for p in py if abs(p[0] - midpoint[0]) < d]
    
    for i in range(len(strip)):
        j = i + 1
        while j < len(strip) and (strip[j][1] - strip[i][1]) < d:
            dist = euclidean_distance(strip[i], strip[j])
            if dist < d:
                d = dist
                min_pair = (strip[i], strip[j])
            j += 1
            
    return d, min_pair

def closest_pair(points):
    if not points or len(points) < 2:
        return None, None
        
    px = sorted(points, key=lambda x: x[0])
    py = sorted(points, key=lambda x: x[1])
    
    min_dist, pair = closest_pair_rec(px, py)
    return round(min_dist, 10), pair
