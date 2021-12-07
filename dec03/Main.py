def partTwo(inputs):
    inputs = list(dict.fromkeys(inputs))
    oxygen = inputs.copy()
    scrubber = inputs.copy()
    for x in range(len(inputs[0])):
        sum = 0
        for y in inputs:
            sum = sum + int(y[x])
        # print(int(y)<<x)
        #print(sum)
        for q in inputs:
            if sum >= len(inputs) / 2:  # most common bit is 1
                if int(q[x]) == 1:
                    # print(q)
                    if q in scrubber and len(scrubber) > 1:
                        scrubber.remove(q)
                else:
                    if (q in oxygen) and (len(oxygen) > 1):
                        oxygen.remove(q)
            else:  # most common bit is 0
                if int(q[x]) == 0:
                    if q in scrubber and len(scrubber) > 1:
                        scrubber.remove(q)
                else:
                    if q in oxygen and len(oxygen) > 1:
                        oxygen.remove(q)

def oxygenGen(inputs):
    oxygen = inputs.copy()
    for x in range(len(oxygen[0])):
        sum = 0
        for x in range(len(oxygen[0])):
            for y in oxygen:
                sum = sum + int(y[x])
            for q in oxygen:
                if sum >= len(oxygen) / 2:  # most common bit is 1
                    if int(q[x]) == 0:
                        if (q in oxygen) and (len(oxygen) > 1):
                            oxygen.remove(q)
                else:  # most common bit is 0
                    if int(q[x]) == 1:
                        if q in oxygen and len(oxygen) > 1:
                            oxygen.remove(q)
        return oxygen
def scrubberGen(inputs):
    scrubber = inputs.copy()
    for x in range(len(scrubber[0])):
        sum = 0
        for y in scrubber:
            sum = sum + int(y[x])
        # print(int(y)<<x)
        # print(sum)
        for q in scrubber:
            if sum >= len(scrubber) / 2:  # most common bit is 1
                if int(q[x]) == 1:
                    if q in scrubber and len(scrubber) > 1:
                        scrubber.remove(q)
            else:  # most common bit is 0
                if int(q[x]) == 0:
                    if q in scrubber and len(scrubber) > 1:
                        scrubber.remove(q)
    return scrubber


#    print(binaryToInt(oxygen))
#    print(binaryToInt(scrubber))
#    print(oxygen)
#    print(scrubber)
#    print("answer to second part: " + str(binaryToInt(oxygen)*binaryToInt(scrubber)))
def binaryToInt(binary):
    input = binary[0]
    out = 0
    for x in range(len(input)):
        if int(input[x]) == 1:
            out = out + 2**(len(binary[0])-1-x)
    return out

def main():
    inputs = open("input.txt").read().splitlines()
    gamma = epsilon = 0
    for x in range(len(inputs[0])):
        if sum([int(i[x]) for i in inputs]) > 500:
            gamma = gamma + 2 ** (11 - x)
        else:
            epsilon = epsilon + 2 ** (11 - x)
    print(gamma * epsilon)
    oxygen = oxygenGen(inputs)
    scrubber = scrubberGen(inputs)
    print(oxygen)
    print(scrubber)



main()
