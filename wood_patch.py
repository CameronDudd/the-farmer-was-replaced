from utils import ternary, mov, plant_simple_patch

def do_wood_patch(x0, y0, x1, y1):
    mov(x0, y0)
    xn = x1 - x0
    for y in range(y1 - y0 + 1):
        row_even = y % 2 == 0
        direction = ternary(row_even, East, West)
        for x in range(xn + 1):
            if can_harvest():
                harvest()
            if get_ground_type() == Grounds.Soil:
                till()
            plant(ternary((x + y) % 2 == ternary(row_even, 0, 1), Entities.Bush, Entities.Tree))
            if x < xn:
                move(direction)
        move(North)

if __name__ == "__main__":
    n = get_world_size() - 1
    while True:
        plant_simple_patch(0, 0, n, n, Entities.Tree)
