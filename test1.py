import csv
import json


#Import map.csv and frame a 2D array
mapData = list(csv.reader(open("map.csv")))
#print(len(mapData))

#Read lane.json and form a list of dictionaries
with open('lane.json') as json_file:
    laneData = json.load(json_file)
#print(laneData)

#Read lane.json and form a list of dictionaries
with open('traffic.json') as json_file:
    traffData = json.load(json_file)
#print(laneData)

#Initialiase indepJunc to hold the information of juctions and their lanes
indepJunc=dict()
for junc in range(len(mapData)):
    indepJunc[junc+1]=[]
#print(indepJunc)
for lane in laneData:
#    print(lane['end1'], "is at the endpoint of 1 of lane", lane['laneId'])
    indepJunc[lane['end1']].append((lane['laneId'],1))
#    print(lane['end2'], "is at the endpoint of 2 of lane", lane['laneId'])
    indepJunc[lane['end2']].append((lane['laneId'],2))
print(indepJunc)
