import re
import numpy as np

def fixInput(input):
    xValues = []
    yValues = []
    for x in input:
        values = re.findall("[0-9]{1,3}", x)
        xValues.append(int(values[0]))
        xValues.append(int(values[2]))
        yValues.append(int(values[1]))
        yValues.append(int(values[3]))
    return xValues, yValues

    return
def removeDiag(x, y):
    ind = len(x)-1
    indexes = []
    for i in range(0,len(x)-1,2):
        z = ind - i
        if x[z] - x[z - 1] != 0 and y[z]-y[z - 1] != 0:
            x.pop(z)
            x.pop(z-1)
            y.pop(z)
            y.pop(z-1)
    return x,y
def fillMap(x,y):
    map = np.zeros((1000,1000))

    for i in range(0, len(x)-1, 2):
        if x[i] != x[i+1]:
            map[x[i]:x[i+1],y[i]] = map[x[i]:x[i+1],y[i]]+1
            print(map[x[i]:x[i+1],y[i]])
            #diff  = np.abs(x[i]-x[i+1])

           # for j in range(diff):
           #     map[x[i+j], y[i]] = map[x[i+j], y[i]] + 1
        else:
            map[x[i], y[i]:y[i+1]] = map[x[i], y[i]:y[i+1]] + 1
            print(map[x[i], y[i]:y[i+1]])
            #diff = np.abs(y[i] - y[i + 1])
            #for j in range(diff):
            #    map[x[i], y[i+j]] = map[x[i], y[i+j]] + 1

    return map

def getMatrix(lines):
    return
def main():
    input = open("input.txt").read().splitlines()
    x, y = fixInput(input)
    newx, newy = removeDiag(x,y)
   # map = np.zeros((1000,1000))
   # map[0,0] = 1
   # map[999,999] = 999
    matrix = fillMap(newx,newy)
    print(map)

main()
