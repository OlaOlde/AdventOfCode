def howmuchincrease(list):
    increase = 0
    for x in range(len(list) -1):
        next = int(list[x+1])
        curr = int(list[x])
        if int(list[x+1]) > int(list[x]):
            increase += 1
    return increase

def makeSummedList(list):
    newList = []
    for x in range(len(list)-2):
        temp = int(list[x]) + int(list[x+1]) + int(list[x+2])
        newList.append(temp)
    return newList

def main():
    depths = open("input.txt").read().splitlines()
    print(howmuchincrease(depths))
    print(howmuchincrease(makeSummedList(depths)))

main()
