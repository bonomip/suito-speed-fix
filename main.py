import sys

from parser.tcx import getMarker
from classes.tcxclasses import Course

course = Course();

#read
with open(sys.argv[1], "r") as file_input:
    for line in file_input:
        marker = str(getMarker(line))
        if( marker != "" ):
            course.update(marker, line)

course.finish();

is_header = True;

lap_count = 0;
lap = course.getLap(0)

tp_count = -1;
tp = 0;

#write
name = sys.argv[1]
name = name[:-4]
with open(sys.argv[1], "r") as file_input:
    with open(name+"_fixed.tcx", "w") as file_output:
        for line in file_input:    
            if is_header :
                if line.lstrip().startswith("<Trackpoint>"):
                    is_header = False
                    tp_count = tp_count + 1
                    tp = lap.getTrackPoint(tp_count);

                if line.lstrip().startswith("<DistanceMeters>"):
                    line = "\t\t\t\t<DistanceMeters>"+str(lap.tot_dist)+"</DistanceMeters>\n"
                
                if line.lstrip().startswith("<MaximumSpeed>"):
                    line = "\t\t\t\t<MaximumSpeed>"+str(lap.max_speed)+"</MaximumSpeed>\n"
                    
            else:
                if line.lstrip().startswith("<Lap StartTime"):
                    lap_count = lap_count + 1;
                    lap = course.getLap(lap_count);
                    is_header = True;
                    tp_count = -1;

                if line.lstrip().startswith("<DistanceMeters>"): #TrackPoint
                    tp.dist += tp.speed
                    line = "\t\t\t\t\t\t<DistanceMeters>"+str(tp.dist)+"</DistanceMeters>\n"
                
                if line.lstrip().startswith("<ns3:Speed>"):
                    line = "\t\t\t\t\t\t\t<ns3:Speed>"+str(tp.speed)+"</ns3:Speed>\n"
                
                if line.lstrip().startswith("<ns3:AvgSpeed>"):
                    line = "\t\t\t\t\t\t<ns3:AvgSpeed>"+str(lap.avg_speed)+"</ns3:AvgSpeed>\n"
            
            file_output.write(line)
