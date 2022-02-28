from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.station import MonitoringStation

def run():
    """requirements for 2C"""

    stations = build_station_list()
    update_water_levels(stations)
    stations = stations_highest_rel_level(stations, 10)

    for station in stations:
        print(station.name, MonitoringStation.relative_water_level(station))

if __name__ == "__main__":
    print("*** Task 2C: CUED Part IA Flood Warning System ***")
    run()