EntityNeedsSoilLookup = {
    Entities.Grass: False,
    Entities.Bush: False,
    Entities.Tree: False,
    Entities.Carrot: True,
    Entities.Pumpkin: True,
    Entities.Sunflower: True,
    Entities.Cactus: True,
}

def restart():
    clear()
    while not can_harvest():
        pass

def xor(a, b):
    return (a or b) and not (a and b)

def ternary(condition, if_true, if_false):
    if condition:
        return if_true
    return if_false

def submov(current_pos, target_pos, direction, inv_direction, max_pos):
    direction_diff = 0
    inv_direction_diff = 0
    if current_pos < target_pos:
        direction_diff = target_pos - current_pos
        inv_direction_diff = (max_pos - target_pos) + current_pos
    else:
        direction_diff = (max_pos - current_pos) + target_pos 
        inv_direction_diff = current_pos - target_pos
    mov_direction = direction
    steps = direction_diff
    if inv_direction_diff < direction_diff:
        mov_direction = inv_direction
        steps = inv_direction_diff
    for _ in range(steps):
        move(mov_direction)

def mov(x, y):
    n = get_world_size()
    submov(get_pos_x(), x, East, West, n)
    submov(get_pos_y(), y, North, South, n)


def do_simple_patch(x0, y0, x1, y1, entity):
    mov(x0, y0)
    for y in range(y0, y1 + 1):
        for x in range(x0, x1 + 1):
            if can_harvest():
                harvest()
            if not (EntityNeedsSoilLookup[entity] and (get_ground_type() == Grounds.Soil)):
                till()
            plant(entity)
            if (x < x1):
                move(East)
        if (y < y1):
            mov(x0, y + 1)
