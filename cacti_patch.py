from utils import restart, mov, plant_simple_patch

def harvest_cacti(x0, y0, x1, y1):
    for y in range(y0, y1 + 1):
        sorted = False
        xmin = x0
        xmax = x1
        while not sorted:
            sorted = True
            for x in range(xmin, xmax):
                mov(x, y)
                if measure() > measure(East):
                    sorted = False
                    swap(East)
                    move(East)
            xmax -= 1
            if sorted:
                break
            for x in range(xmax, xmin, -1):
                mov(x, y)
                if measure() < measure(West):
                    sorted = False
                    swap(West)
                    move(West)
            xmin += 1
    for x in range(x0, x1 + 1):
        sorted = False
        ymin = x0
        ymax = y1
        while not sorted:
            sorted = True
            for y in range(ymin, ymax):
                mov(x, y)
                if measure() > measure(North):
                    sorted = False
                    swap(North)
                    move(North)
            ymax -= 1
            if sorted:
                break
            for y in range(ymax, ymin, -1):
                mov(x, y)
                if measure() < measure(South):
                    sorted = False
                    swap(South)
                    move(South)
            ymin += 1
    mov(x1, y1)
    while not can_harvest():
        continue
    harvest()

def plant_cacti_patch(x0, y0, x1, y1):
    plant_simple_patch(x0, y0, x1, y1, Entities.Cactus)

if __name__ == "__main__":
    n = 5 
    restart()
    while True:
        plant_cacti_patch(0, 0, n, n)
        harvest_cacti(0, 0, n, n)
