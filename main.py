from utils import restart, plant_simple_patch
from wood_patch import do_wood_patch
from pumpkin_patch import plant_pumpkin_patch, scan_bad_pumpkins, harvest_pumpkins
from sunflower_patch import plant_sunflower_patch, harvest_sunflower_patch

if __name__ == "__main__":
    restart()
    while True:
        plant_simple_patch(6, 6, 15, 10, Entities.Grass)
        plant_simple_patch(6, 11, 15, 15, Entities.Carrot)
        do_wood_patch(0, 6, 5, 15)
        plant_pumpkin_patch(0, 0, 5, 5)
        sunflower_order = plant_sunflower_patch(6, 0, 15, 5)
        bad_pumpkins = scan_bad_pumpkins(0, 0, 5, 5)
        harvest_pumpkins(bad_pumpkins)
        harvest_sunflower_patch(sunflower_order)
