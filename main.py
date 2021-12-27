#import tkinter as tk
import random

# pak smazat
def printBoard(matrix):
    for i in range(4):
        print(*matrix[i])
    print('-------')

def newTile(matrix):
    counter = 0
    for row in range(4):
        for column in range(4):
            if matrix[row][column] != 0:
                counter += 1
    if counter == 16:
        # TODO: osetrit pripady, kdy se nemuzu hnout, ale existuje move protoze ->
        print('You lost') # not really... kdyz uz se nemuzu nikam hnout tak jsem prohrala, ne kdyz se zaplni vsechna policka
        return 

    row = random.randrange(4)
    column = random.randrange(4)
    if matrix[row][column] == 0:
        matrix[row][column] = random.choice([2,4])
    else:
        newTile(matrix)
    return matrix

def newGame(matrix):
    sim_matrix = [[2,0,16,0],[0,0,16,2],[2,4,0,0],[2,4,16,0]]
    matrix = sim_matrix  #[[0] * 4 for _ in range(4)]
    newTile(matrix)

    # pak smazat
    printBoard(matrix)

    return matrix

#####

# noodle = row/column
def mergeNoodle(n1,n2,n3,n4):
# nejdriv zmergeuju, potom posunu na nulovy mista, delam slide k n1 !!!
# TODO: rozdelit opakující se úseky na menší funkce
    noodle = [n1, n2, n3, n4]
    newNoodle = []
    counter = 4
    for num in noodle:
        if num != 0:
            newNoodle.append(num)
            counter -= 1
    nulls = [0] * counter
    noodle = newNoodle + nulls
    
    if noodle[0] == noodle[1]: 
        noodle[0] *= 2
        noodle[1] = 0
    if noodle[1] == noodle[2]: 
        noodle[1] *= 2
        noodle[2] = 0
    if noodle[2] == noodle[3]: 
        noodle[2] *= 2
        noodle[3] = 0

    newNoodle = []
    counter = 4
    for num in noodle:
        if num != 0:
            newNoodle.append(num)
            counter -= 1
    nulls = [0] * counter

    return newNoodle + nulls

def down(matrix):
    newMatrix = [[],[],[],[]]
    for row in range(4):
        noodle = [mergeNoodle(matrix[3][row],matrix[2][row],matrix[1][row],matrix[0][row])][0][::-1]
        for j in range(4):
            newMatrix[j] += [noodle[j]]
    printBoard(newMatrix)
    newTile(newMatrix)

def up(matrix):
    newMatrix = [[],[],[],[]]
    for row in range(4):
        noodle = mergeNoodle(matrix[0][row],matrix[1][row],matrix[2][row],matrix[3][row])
        for j in range(4):
            newMatrix[j] += [noodle[j]]
    printBoard(newMatrix)
    newTile(newMatrix)

def left(matrix):
    newMatrix = []
    for row in range(4):
        newMatrix += [mergeNoodle(matrix[row][0],matrix[row][1],matrix[row][2],matrix[row][3])]
    newTile(newMatrix)

def right(matrix):
    newMatrix = []
    for row in range(4):
        newNoodle = [mergeNoodle(matrix[row][3],matrix[row][2],matrix[row][1],matrix[row][0])]
        newMatrix += [newNoodle[0][::-1]]
    newTile(newMatrix)

matrix = [[2, 0, 16, 2], [0, 0, 16, 2], [2, 4, 0, 0], [2, 4, 16, 0]]
#newGame(matrix)
down(matrix)

#print(mergeNoodle(2,2,2,2))