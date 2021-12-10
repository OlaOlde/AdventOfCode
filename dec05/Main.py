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
def removeDiag(lines):
    return
def getMatrix(lines):
    return
def main():
    input = open("input.txt").read().splitlines()
   # x = map(fixInput, input)
   # print(list(x))
    #x, y = map(fixInput, input) #(input[0])
    x, y = fixInput(input)
    print(x)
    print(y)
main()
