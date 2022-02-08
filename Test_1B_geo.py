from floodsystem.geo import stations_by_river
from floodsystem.geo import stations_by_river, stations_by_distance
from floodsystem.stationdata import build_station_list
#Input a co-ordinate tuple, p
print("Insert co-ordinates. Lat, then long")
x=float(input())
y=float(input())
p= (x,y)
#create a list of stations
stations = build_station_list()


def test_stations_by_distance(stations, p):
   """This function returns a sorted list of stations a distance 'x' from a given co-ordinate, 'p'"""
    stationname=[]
    from haversine import haversine, Unit
    stationdist=[]
    for station in stations:
        stationdist.append(haversine(station.coord, p))
        stationname.append(station.name)
    stations=list(zip(stationname, stationdist))
    stations.sort(key=lambda x: x[1])
    return stations
  
 print (test_stations_by_distance(stations, 
