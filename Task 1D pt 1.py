from floodsystem.geo import stations_by_river, rivers_with_station
from floodsystem.stationdata import build_station_list

def run():
    """Requirements for Task 1D"""
     #Build list of stations 
    stations = build_station_list()

    #build a list of the list given at the end of 1D.1
    rivwstat= list(rivers_with_station(stations))

    #print number of rivers with at least one station
    print(len(rivwstat))

    #print alphabetical list of the first 10 rivers with a station
    rivwstat.sort()
    for i in range(10):
        print(rivwstat[i])

if __name__ == "__main__":
    print("*** Task 1D Part 1: CUED Part IA Flood Warning System ***")
    run()
