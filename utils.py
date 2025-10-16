def restart():
    clear()
    while not can_harvest():
        pass

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
