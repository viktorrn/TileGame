import math
import os
import map
import io

os.system("cls")

mapWidth = 10
mapHeight = 10
gameRunning = True
tileMaps = map.initMap(mapWidth, mapHeight)

while gameRunning:
    os.system("cls")
    map.drawMap(tileMaps, mapWidth, mapHeight)
    print("\n [W]:UP\t[A]:LEFT\t[D]:RIGHT\t[S]:DOWN\t[F]:ATTACK")
    inp = input(" ")


        


