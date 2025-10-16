from utils import restart, mov, do_simple_patch

def scan_bad_pumpkins(x0, y0, x1, y1):
    mov(x0, y0)
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

def do_pumpkin_patch(x0, y0, x1, y1):
    do_simple_patch(x0, y0, x1, y1, Entities.Pumpkin)
    bad_pumpkins = scan_bad_pumpkins(x0, y0, x1, y1)  # TODO: Check bad pumpkins in sliding window
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

if __name__ == "__main__":
    restart()
    while True:
        do_pumpkin_patch(0, 0, 5, 5)
