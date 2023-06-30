#!/usr/bin/env python3

import sys
import math

Lat = sys.argv[1]
Lon = sys.argv[2]
Hei = sys.argv[3]

Lat = float(Lat)
Lon = float(Lon)
Hei = float(Hei)

a = 6378137
f = 1/298.257223563

cosLat = math.cos(Lat*math.pi/180)
sinLat = math.sin(Lat*math.pi/180)

cosLon = math.cos(Lon*math.pi/180)
sinLon = math.sin(Lon*math.pi/180)


c = 1 / math.sqrt(cosLat * cosLat + (1 - f) * (1 - f) * sinLat * sinLat)
s = (1 - f) * (1 - f) * c

X = (a*c+Hei) * cosLat * cosLon
Y = (a*c+Hei) * cosLat * sinLon
Z = (a*s+Hei) * sinLat

print("X: "+str(X)+"\tY: "+str(Y)+"\tZ: "+str(Z))


