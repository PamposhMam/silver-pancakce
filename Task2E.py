from floodsystem.plot import plot_water_levels
from floodsystem.stationdata import build_station_list
stations= build_station_list()
dates= 0
levels=0
print(plot_water_levels("Cam", dates, levels))
