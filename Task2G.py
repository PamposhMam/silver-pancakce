
import datetime

from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import towns_by_rel_levels, floodWarning

def run():
    "2G"

    stations = build_station_list()
    update_water_levels(stations)

    # get list of (town, highest rel lev, rel predicted lev change) tuples, in descending order, for towns above 0.8
    towns = towns_by_rel_levels(stations)

    #print(sorted([town[2] for town in towns]))

    # assign risk rating to each town
    # there are anomolies in the relative levels (600, -16 etc. typical range 2.5 - -1.5)
    print('\n***FLOOD WARNINGS***\n')

    for town in towns:
        floodWarning(town)
        #print(town[1], town[2])

    return

if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()

