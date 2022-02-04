from floodsystem.station import inconsistent_typical_range_stations
from floodsystem.stationdata import build_station_list

def run():
    """Requirements for Task 1F"""

    # Build list of stations
    stations = build_station_list()

    # Get list of stations with inconsistent range data
    inconsistentStations = [station.name for station in inconsistent_typical_range_stations(stations)]
    
    # Sort names into alphabetical order
    inconsistentStations.sort()

    print(inconsistentStations)

if __name__ == "__main__":
    print("*** Task 1F: CUED Part IA Flood Warning System ***")
    run()