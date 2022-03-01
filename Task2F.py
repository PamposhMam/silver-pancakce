import datetime

from floodsystem.analysis import polyfit
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.flood import stations_highest_rel_level

def run():
    """Requirements for Task 2F"""

    # Build list of stations
    stations = build_station_list()
    update_water_levels(stations)

    highRiskStations = stations_highest_rel_level(stations, 5)
    
    for i in range(5):
        #for station in highRiskStations:
            # Fetch data over past 2 days
        dt = 2
        dates, levels = fetch_measure_levels(
            highRiskStations[i].measure_id, dt=datetime.timedelta(days=dt))

        # Check that data could bbe found. Return if not found.
        if not dates or not levels:
            print('No data available for Station {}'.format(highRiskStations[i].name))
            continue

        plot_water_level_with_fit(highRiskStations[i], dates, levels, 4)

if __name__ == "__main__":
    print("*** Task 2F: CUED Part IA Flood Warning System ***")
    run()