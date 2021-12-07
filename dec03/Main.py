def main():
    inputs = open("input.txt").read().splitlines()
    gamma = epsilon = 0
    for x in range(len(inputs[0])):
        if sum([int(i[x]) for i in inputs]) > 500:
            gamma = gamma + 2**(11-x)
        else:
            epsilon = epsilon + 2**(11-x)
    print(gamma*epsilon)
main()
