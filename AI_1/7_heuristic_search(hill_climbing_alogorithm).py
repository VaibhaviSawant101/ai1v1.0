import random

N = int(input("Enter value of N in N-Queens Problem "))


def checkPossibility(chessBoard, i, j):
    for row in range(len(chessBoard)):
        for element in range(len(chessBoard[row])):
            if chessBoard[row][element] == 'Q':
                jDist = abs(j - element)
                iDist = abs(i - row)
                if i == row or j == element or jDist == iDist:
                    return False
    return True


def hueristicFunction(chessBoard, goal, i, j):
    count = 0
    for row in chessBoard:
        for element in row:
            if element == 'Q':
                count += 1
    if i != -1 and j != -1:
        count += 1

    return (goal - count)


chessBoard = [['-'] * N for i in range(N)]

while hueristicFunction(chessBoard, N, -1, -1) != 0:  # loop to perform random placing
    chessBoard = [['-'] * N for i in range(N)]
    for row in range(len(chessBoard)):
        dist = -1
        i = -1
        j = -1
        resultList = []
        for element in range(len(chessBoard[row])):
            if checkPossibility(chessBoard, row, element):
                hDist = hueristicFunction(chessBoard, N, row, element)
                if dist <= hDist:
                    dist = hDist
                    i = row
                    j = element
                    resultList.append([row, element])
        if len(resultList) > 0:
            idex, jdex = resultList[random.randint(0, len(resultList) - 1)]
            print("\n i index=", idex, "\n j index=", jdex)
            chessBoard[idex][jdex] = 'Q'
        for row1 in chessBoard:
            print("\t", row1)
        print("Heuristic value is: ", hueristicFunction(chessBoard, N, -1, -1))

print("Heuristic value is: ", hueristicFunction(chessBoard, N, -1, -1), "\n")
print("\nFollowing is the Global maxima solution for", N, "Queen Problem with heuristic distance from goal state =",
      hueristicFunction(chessBoard, N, -1, -1), "\n\n")

for row1 in chessBoard:
    print("\t", row1)

print("\n")


# Algorithm for Simple Hill Climbing:
# Step 1: Evaluate the initial state, if it is goal state then return success and Stop.
# Step 2: Loop Until a solution is found or there is no new operator left to apply.
# Step 3: Select and apply an operator to the current state.
# Step 4: Check new state:
#   If it is goal state, then return success and quit.
#   Else if it is better than the current state then assign new state as a current state.
#   Else if not better than the current state, then return to step2.
# Step 5: Exit.