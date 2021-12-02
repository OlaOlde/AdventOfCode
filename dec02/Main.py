
def secondPuzzle(input):
    aim = 0
    vPos = 0
    hPos = 0
    for command in input:
        x = command.split()
        steps = int(x[1])
        if x[0] == 'forward':
            hPos = hPos + steps
            vPos = vPos + steps * aim
        elif x[0] == 'up':
            aim = aim - steps
        elif x[0] == 'down':
            aim = aim + steps
    print("answer to second puzzle: " + str(vPos * hPos))
def main():
    inputs = open("input.txt").read().splitlines()
    verticalPos = 0
    horizontalPos = 0
    aim = 0
    for command in inputs:
        x = command.split()
        steps = int(x[1])
        #dir = str(x[0])
        if x[0] == 'forward':
            horizontalPos = horizontalPos + steps
        elif x[0] == 'up':
            verticalPos = verticalPos - steps
        elif x[0] == 'down':
            verticalPos = verticalPos + steps
    print("answer to first puzzle: "+ str(verticalPos*horizontalPos))
    secondPuzzle(inputs)
main()
