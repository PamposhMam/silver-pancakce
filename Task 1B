from floodsystem.geo import stations_by_river
from floodsystem.stationdata import build_station_list
def run():
    #Input a co-ordinate tuple, p
    print("Insert co-ordinates. Lat, then long")
    x=float(input())
    y=float(input())
    p= (x,y)
    #create a list of stations
    stations = build_station_list()

    #create a list of tuples: station name, town, distance
    stationlist= stations_by_distance(stations)
    list1, list2= zip(*stationlist)
    list3=[]
    for i in len(stations-1):
        if station.name(i)==list1(i):
            list3(i)=station.town(i)
    stationlistfinal= list(zip(list1, list3, list2))
    #print the 10 closest stations
    for i in range(0:10):
        print stationlistfinal(i)

    #print the 10 furthest stations
    for i in range(:len(stationlistfinal)-10):
        print stationlistfinal(i)
if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()

