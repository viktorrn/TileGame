import sys
import math
import os

def  initMap(  mapHeight,  mapWidth  ):
    tileMap = []
    for r in range(mapHeight):
        row = []
        for c in range(mapWidth):
            row.append(' ')
        tileMap.append(row)   
    return tileMap

def drawMap(tileMap, mapHeight, mapWidth):
    for r in range(mapHeight):
        for c in range(mapWidth):
            if (r % mapWidth == 0) or (c % mapHeight == 0):
                tileMap[r][c] = ' #'
            else:
                tileMap[r][c] = ' '
            
    for r in range(mapHeight):
        
        for c in range(mapWidth):
            sys.stdout.write(tileMap[r][c])

        sys.stdout.write('\n')
