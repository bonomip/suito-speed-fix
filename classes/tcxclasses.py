from bmath.mathbike import iterVel
from parser.tcx import getData

class TrackPoint:

    def __init__(self):
        self.speed = 0
        self.cadence = 0
        self.dist = 0;



    def update(self, marker, value, line):
        if( marker == "ns3:Watts" ):                    
            self.speed = iterVel(int(value), 20/3.6)
        if ( marker == "Cadence"):
            self.cadence = int(value);

class Lap:

    def __init__(self):
        self.tps = [TrackPoint()];
        self.tot_dist = 0;
        self.max_speed = 0
        self.avg_speed = 0
        self.avg_cad = 0
        self.count = -1

    def update(self, marker, line):
        if ( marker == "Trackpoint" ):
            self.tps.append(TrackPoint())
        else:
            self.tps[-1].update(marker, getData(line, marker), line)

    def finish(self):
        for tr in self.tps:
            if tr.speed > self.max_speed:
                self.max_speed = tr.speed

            self.tot_dist += tr.speed
            self.count = self.count + 1
            self.avg_cad += tr.cadence
            self.avg_speed += tr.speed

        self.avg_speed /= self.count
        self.avg_cad /= self.count

        print(self.avg_cad)
    
    def getTrackPoint(self, index):
        return self.tps[index+1];

class Course:

    def __init__(self):

        self.laps = [Lap()];

    def update(self, marker, line):
        if ( marker[0:3] == "Lap"):
            self.laps.append(Lap());
        else:
            self.laps[-1].update(marker, line)

    def finish(self):
        for lp in self.laps[1:]:
            lp.finish();

    def getLap(self, index):
        return self.laps[index+1];

