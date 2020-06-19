import csv
import json

def sortlist(samplelist):
    #samplelist=[('a', 2, 2), ('b', 1, 1), ('e', 1, 6)]
    sortedlist= sorted(samplelist, key=lambda tup: tup[2])
    return(sortedlist)

def edf(sortJunc):
    print("")
    print("--------------------------------------------------------------------------------------------")
    print("Time      :"+" 12:00 |  12:02 |  12:04 |  12:06 |  12:08 |  12:10 |  12:12 |  12:14 |  12:16 ")
    print("--------------------------------------------------------------------------------------------")
    for i in sortJunc:
        j=sortJunc[i]
        print("Junction "+str(i)+":",end='  ')
        for k in j:
            print((k[0]+str(k[1])+'   |   ')*k[2],end='')
        print()
    
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
    print(lane['dens1'],"is the density of end 1 of lane", lane['laneId'])
    indepJunc[lane['end1']].append((lane['laneId'],1,lane['dens1']))
#    print(lane['end2'], "is at the endpoint of 2 of lane", lane['laneId'])
    print(lane['dens2'],"is the density of end 2 of lane", lane['laneId'])
    indepJunc[lane['end2']].append((lane['laneId'],2,lane['dens2']))
print("")
print(indepJunc)
print("")
sortJunc=dict()
for lists in indepJunc:
    ans=sortlist(samplelist[lists])
    print(ans)
    sortJunc[lists]=ans
print(sortJunc)
edf(sortJunc)




