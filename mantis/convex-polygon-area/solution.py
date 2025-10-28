def polygon_area(vertices):
    """
    Calculates area of convex polygon using Shoelace formula.
    Time: O(n), Space: O(1)
    """
    if len(vertices) < 3:
        return 0.0

    n = len(vertices)
    area = 0.0

    for i in range(n):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % n]  # Wrap around to first vertex
        area += (x1 * y2) - (x2 * y1)

    return round(abs(area) / 2.0, 6)
