from floodsystem.geo import stations_by_river
from floodsystem.stationdata import build_station_list

def run():
    """Requirements for Task 1D"""

    # Build list of stations
    stations = build_station_list()

    # Print the names of the stations located on 3 rivers in alphabetical order
    rivers = ['River Aire', 'River Cam', 'River Thames']
    
    for river in rivers:
        stationsOnRiver = stations_by_river(stations)[river]
        names = [stationsOnRiver[i].name for i in range(len(stationsOnRiver))]
        names.sort()
        print('\nRiver: {}'.format(river))
        print(names)

if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()