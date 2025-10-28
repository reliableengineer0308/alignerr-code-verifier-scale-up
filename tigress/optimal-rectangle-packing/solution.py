def optimal_rectangle_packing(rectangles):
    """
    Packs rectangles into minimal area bounding box.
    
    Args:
        rectangles: List of (width, height) tuples
    
    Returns:
        tuple: (min_area, list of (x, y, w, h) placements)
    """
    if not rectangles:
        return 0, []
    
    # For small inputs (<= 10), use backtracking with pruning
    if len(rectangles) <= 10:
        return _backtrack_packing(rectangles)
    else:
        # For larger inputs, use First-Fit Decreasing heuristic
        return _ffd_packing(rectangles)



def _backtrack_packing(rectangles):
    """Exact solution using backtracking with pruning."""
    rectangles = sorted(rectangles, key=lambda r: r[0] * r[1], reverse=True)
    n = len(rectangles)
    best_area = float('inf')
    best_placement = []

    def is_overlap(r1, r2):
        """Check if two rectangles overlap."""
        x1, y1, w1, h1 = r1
        x2, y2, w2, h2 = r2
        return not (x1 + w1 <= x2 or x2 + w2 <= x1 or
                  y1 + h1 <= y2 or y2 + h2 <= y1)

    def can_place(rect, pos_x, pos_y, placement):
        """Check if rect can be placed at (pos_x, pos_y) without overlap."""
        new_rect = (pos_x, pos_y, rect[0], rect[1])
        for placed in placement:
            if is_overlap(new_rect, placed):
                return False
        return True

    def update_bounding_box(placement):
        """Calculate bounding box for current placement."""
        if not placement:
            return 0, 0
        max_x = max(r[0] + r[2] for r in placement)
        max_y = max(r[1] + r[3] for r in placement)
        return max_x, max_y

    def backtrack(index, placement):
        nonlocal best_area, best_placement
        if index == n:
            width, height = update_bounding_box(placement)
            area = width * height
            if area < best_area:
                best_area = area
                best_placement = placement[:]
            return

        rect = rectangles[index]
        width, height = update_bounding_box(placement) if placement else (0, 0)

        # Try placing at all candidate positions
        # Candidate x: 0 and all right edges of placed rects
        # Candidate y: 0 and all top edges of placed rects
        x_candidates = {0}
        y_candidates = {0}
        for r in placement:
            x_candidates.add(r[0] + r[2])
            y_candidates.add(r[1] + r[3])

        for x in sorted(x_candidates):
            for y in sorted(y_candidates):
                if can_place(rect, x, y, placement):
                    placement.append((x, y, rect[0], rect[1]))
                    backtrack(index + 1, placement)
                    placement.pop()

    backtrack(0, [])
    return best_area, best_placement



def _ffd_packing(rectangles):
    """Heuristic solution using First-Fit Decreasing."""
    # Sort by area descending
    sorted_rects = sorted(rectangles, key=lambda r: r[0]*r[1], reverse=True)
    placement = []
    used_positions = set()

    for rect in sorted_rects:
        w, h = rect
        # Find first available position (leftmost, bottommost)
        placed = False
        for y in range(100):  # Arbitrary limit
            for x in range(100):
                if (x, y) in used_positions:
                    continue
                # Check if rectangle fits at (x,y)
                if all((nx, ny) not in used_positions
                       for nx in range(x, x+w)
                       for ny in range(y, y+h)):
                    # Place rectangle
                    for nx in range(x, x+w):
                        for ny in range(y, y+h):
                            used_positions.add((nx, ny))
                    placement.append((x, y, w, h))
                    placed = True
                    break
            if placed:
                break

    # Calculate bounding box
    if placement:
        max_x = max(p[0] + p[2] for p in placement)
        max_y = max(p[1] + p[3] for p in placement)
        area = max_x * max_y
    else:
        area = 0

    return area, placement
