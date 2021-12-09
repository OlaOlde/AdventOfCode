import numpy as np
def score(board, nbrs):
    shape = (5, 5)
    matrix = np.zeros(shape)
    for q in range(5):
        row = board[q].split()
        for z in range(5):
            matrix[[q],[z]]= int(row[z])
    checkMatrix = np.zeros(shape)
    ind = 0
    for x in nbrs:
        y = np.where(matrix == int(x))
        ind = ind + 1
        if y[0].size != 0:
            checkMatrix[y[0],y[1]] = 1
            if(checkBingo(checkMatrix)):
                tempMatrix = 1-checkMatrix
                scoreMatrix = tempMatrix*matrix
                score = sum(sum(scoreMatrix))*int(x)

                return int(score), ind
def checkBingo(matrix):
    s = matrix.shape
    bingoCol = np.where(matrix.sum(axis=0) == s[0])
    bingoRow = np.where(matrix.sum(axis=1) == s[1])
    if len(bingoRow[0]) != 0 or len(bingoCol[0]) != 0:
        return True
    else:
        return False
def main():
    boards = open("boards.txt").read().splitlines()
    numbers = open("numbers.txt").read().split(',')
    scores = []
    indices = []
    for x in range(int(len(boards)/6)):
        tempScore, ind = score(boards[(x*6):(x*6)+5],numbers)
        scores.append(tempScore)
        indices.append(ind)
    minInd = np.argmin(indices)
    maxInd = np.argmax(indices)
    print("puzzle 1 ans: " + str(scores[minInd]))
    print("puzzle 2 ans: " + str(scores[maxInd]))

main()
