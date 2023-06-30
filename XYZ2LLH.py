#!/usr/bin/env python3
import sys
import math

# Input über Kommandozeile
X = sys.argv[1]
Y = sys.argv[2]
Z = sys.argv[3]

X = float(X)
Y = float(Y)
Z = float(Z)

# WGS84-Parameter
a = 6378137
f = 1/298.257223563

# Eigentliche Umrechung

e = math.sqrt(2*f - f**2)
h = 0
N = 1

for i in range(0,8):
    
    phi = math.atan2(Z, math.sqrt(X**2+Y**2) * (1-e**2*N/(N+h)))

    N = a/math.sqrt(1-e**2*(math.sin(phi))**2)

    h = (math.sqrt(X**2+Y**2)/math.cos(phi)) - N

lam = math.atan2(Y,X)

print("Lat: " +str(phi*180/math.pi) +"\tLon: " +str(lam*180/math.pi) +"\tHeight: "+ str(h))


