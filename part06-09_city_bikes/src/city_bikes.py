# tee ratkaisu tänne
# Write your solution here
import math
def get_station_data(filename: str):
    dictionary={}
    with open(filename) as bikes_file:
        for line in bikes_file:
            line=line.split(";")
            if line[0]=="Longitude":
                continue
            dictionary[line[3]]=(float(line[0]),float(line[1]))
    return dictionary

def distance(stations: dict, station1: str, station2: str):
    xkm=(stations[station1][0]-stations[station2][0])*55.26
    ykm=(stations[station1][1]-stations[station2][1])*111.2
    distance=math.sqrt(xkm**2+ykm**2)
    return distance

def greatest_distance(stations: dict):
    station1,station2,greatestDist=('','',0)
    listOfStations=[]
    for (item,val) in stations.items():
        listOfStations.append([item,val])
    for i in range(len(listOfStations)):
        for j in range(i+1,len(listOfStations)):
            dist=distance(stations,listOfStations[i][0],listOfStations[j][0])
            if dist>greatestDist:
                station1=listOfStations[i][0]
                station2=listOfStations[j][0]
                greatestDist=dist
    return (station1,station2,greatestDist)