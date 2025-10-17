from utils import ternary, mov, bisect_left

def harvest_sunflower_patch(sunflowers):
    if len(sunflowers) < 6:
        return
    for x, y in sunflowers[::-1]:
        mov(x, y)
        while not can_harvest():
            continue
        harvest()

def plant_sunflower_patch(x0, y0, x1, y1):
    mov(x0, y0)
    xn = x1 - x0
    positions = []
    num_petals = []
    for y in range(y1 - y0 + 1):
        row_even = y % 2 == 0
        direction = ternary(row_even, East, West)
        for x in range(xn + 1):
            if can_harvest():
                harvest()
            if get_ground_type() == Grounds.Grassland:
                till()
            plant(Entities.Sunflower)
            petals = measure()
            idx = bisect_left(num_petals, petals, 0, len(num_petals))
            num_petals.insert(idx, petals)
            positions.insert(idx, (ternary(row_even, x0 + x, x1 - x), y0 + y))
            if (x < xn):
                move(direction)
        move(North)
    return positions
