def getData(line, marker):
    start = line.find("<"+marker+">") + len("<"+marker+">")
    end = line.find("</"+marker+">")
    return line[start:end]

def getMarker(line):
    if(line.lstrip().startswith("<")):
        start = line.find("<") + len("<")
        end = line.find(">")
        if( start == -1 or end == -1 ):
            return ""
        return line[start:end]