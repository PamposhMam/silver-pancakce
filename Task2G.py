
import datetime

from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import towns_by_rel_levels

def run():
    "2G"

    stations = build_station_list()
    update_water_levels(stations)

    # get list of (town, highest rel lev) tuples, in descending order
    towns = towns_by_rel_levels(stations)
    print(towns)

    # assign risk rating to each town

    # factor in predicted change

    return

if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()