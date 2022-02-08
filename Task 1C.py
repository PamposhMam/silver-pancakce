from floodsystem.geo import stations_by_river
from floodsystem.stationdata import build_station_list
def run():
    #Build a list of stations
    stations = build_station_list()
    #compile a list of stations radius r from Cambridge city centre
    centre= (52.2053, 0.1218)
    cam= list(stations_within_radius(stations, centre, 10))
    #sort the list and print it
    camsort= cam.sort()
    print(camsort())

if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run()
