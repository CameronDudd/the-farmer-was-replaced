from utils import mov, plant_simple_patch, ternary

def harvest_pumpkins(bad_pumpkins):
    while len(bad_pumpkins) > 0:
        tmp = set()
        for x, y in bad_pumpkins:
            mov(x, y)
            if (get_entity_type() == Entities.Dead_Pumpkin):
                plant(Entities.Pumpkin)
                tmp.add((x, y))
            elif not can_harvest():
                tmp.add((x, y))
        bad_pumpkins = tmp
    harvest()

def scan_bad_pumpkins(x0, y0, x1, y1):
    mov(x0, y0)
    xn = x1 - x0
    bad_pumpkins = set()
    for y in range(y1 - y0 + 1):
        row_even = y % 2 == 0
        direction = ternary(row_even, East, West)
        for x in range(xn + 1):
            if get_entity_type() == Entities.Dead_Pumpkin:
                plant(Entities.Pumpkin)
                bad_pumpkins.add((ternary(row_even, x0 + x, x1 - x), y0 + y))
            elif not can_harvest():
                bad_pumpkins.add((ternary(row_even, x0 + x, x1 - x), y0 + y))
            if (x < xn):
                move(direction)
        move(North)
    return bad_pumpkins

def plant_pumpkin_patch(x0, y0, x1, y1):
    plant_simple_patch(x0, y0, x1, y1, Entities.Pumpkin)
