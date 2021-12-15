import re


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
    ind = len(x)
    for i in range(0,len(x)-2,2):
        ind = ind - i
        if x[ind] - x[ind - 1] != 0 and y[ind]-y[ind - 1] != 0:
            x[ind-1:ind] = []
            y[ind-1:ind] = []
    return x, y
def getMatrix(lines):
    return
def main():
    input = open("input.txt").read().splitlines()
   # x = map(fixInput, input)
   # print(list(x))
    #x, y = fixUnput(input) #(input[0])
    x, y = fixInput(input)
    #print(x)
    #print(y)
    print(len(x))
   # z = [0, 1,2,3,4,5,6,7,9]
   # print(z)
   # print(len(z))

   # newx, newy = removeDiag(x,y)
main()
