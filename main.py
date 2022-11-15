import sys

from bmath.mathbike import iterVel
from parser.tcx import getData
from parser.tcx import getMarker

class TrackPoint:
    speed = 0
    cadence = 0

    def update(self, line, marker):
        if( marker == "ns3:Watts" ):
            self.speed = iterVel(int(getData(line, marker)), 20/3.6)
        if ( marker == "Cadence"):
            self.cadence = int(getData(line, marker))

tot_dist = 0
array = []
array.append(TrackPoint())

#read
with open(sys.argv[1], "r") as file_input:
    for line in file_input:
        marker = str(getMarker(line))
        if( marker == "" ):
            continue
        if ( marker == "Trackpoint" ):
            array.append(TrackPoint())
        else:
            array[-1].update(line, marker)

tot_dist = 0
max_speed = 0
avg_speed = 0
avg_cad = 0
count = -1

for tr in array:
    if tr.speed > max_speed:
        max_speed = tr.speed

    tot_dist += tr.speed
    count = count + 1
    avg_cad += tr.cadence
    avg_speed += tr.speed

avg_speed /= count
avg_cad /= count

h = True
count = 0

#write
name = sys.argv[1]
name = name[:-4]
with open(sys.argv[1], "r") as file_input:
    with open(name+"_fixed.tcx", "w") as file_output:
        distance = 0
        for line in file_input:
            if line.lstrip().startswith("<Cadence>") and h:
                line = "<Cadence>"+str(avg_cad)+"</Cadence>"
            if line.lstrip().startswith("<Trackpoint>"):
                h = False
                count = count + 1
            if line.lstrip().startswith("<DistanceMeters>") and h: #header
                line = "<DistanceMeters>"+str(tot_dist)+"</DistanceMeters>"
            if line.lstrip().startswith("<MaximumSpeed>") and h:
                line = "<MaximumSpeed>"+str(max_speed)+"</MaximumSpeed>"
            if line.lstrip().startswith("<DistanceMeters>") and not h: #TrackPoint
                distance += array[count].speed
                line = "<DistanceMeters>"+str(distance)+"</DistanceMeters>"
            if line.lstrip().startswith("<ns3:Speed>") and not h:
                line = "<ns3:Speed>"+str(array[count].speed)+"</ns3:Speed>"
            if line.lstrip().startswith("<ns3:AvgSpeed>"):
                line = "<ns3:AvgSpeed>"+str(avg_speed)+"</ns3:AvgSpeed>"
            file_output.write(line)
