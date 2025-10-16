from utils import restart, mov

def init_pumpkin_patch(x0, y0, x1, y1):
    for y in range(y0, y1 + 1):
        for x in range(x0, x1 + 1):
            if can_harvest():
                harvest()
            if (get_ground_type() == Grounds.Grassland):
                till()
            plant(Entities.Pumpkin)
            if (x < x1):
                move(East)
        if (y < y1):
            mov(x0, y + 1)
    mov(x0, y0)

def scan_bad_pumpkins(x0, y0, x1, y1):
    bad_pumpkins = set()
    for y in range(y0, y1 + 1):
        for x in range(x0, x1 + 1):
            if get_entity_type() == Entities.Dead_Pumpkin:
                bad_pumpkins.add((x, y))
            if (x < x1):
                move(East)
        if (y < y1):
            mov(x0, y + 1)
    return bad_pumpkins

def do_pumpkin_patch(start, end):
    x0, y0 = start
    x1, y1 = end
    mov(x0, y0)
    init_pumpkin_patch(x0, y0, x1, y1)
    bad_pumpkins = scan_bad_pumpkins(x0, y0, x1, y1)
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
    mov(x0, y0)

if __name__ == "__main__":
    restart()
    while True:
        do_pumpkin_patch((0, 0), (5, 5))
