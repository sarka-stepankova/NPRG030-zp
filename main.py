import random
#import tkinter as tk

# pak smazat
def printBoard(matrix):
    for i in range(4):
        print(*matrix[i])
    print('-------')

def newTile(matrix):
    # presne nevím jestli kdyz se dostanu na konec hry, tak bude potreba tohle kontrolovat nebo ne
    # TODO: rozmyslet si funci kódu ř.12-18
    counter = 0
    for row in range(4):
        for column in range(4):
            if matrix[row][column] != 0:
                counter += 1
    if counter == 16:
        return matrix

    row = random.randrange(4)
    column = random.randrange(4)
    if matrix[row][column] == 0:
        matrix[row][column] = random.choice([2,4])
    else:
        newTile(matrix)
    return matrix

def newGame():
    matrix = [[0] * 4 for _ in range(4)]
    newTile(matrix)

    # pak smazat, nahradit grafickým překreslením
    #printBoard(matrix)
    return matrix

# Check whether you lost or win

def horizontalMoveExists(matrix):
    for row in range(4):
        for column in range(3):
            if matrix[row][column] == matrix[row][column + 1]:
                return True
    return False

def verticalMoveExists(matrix):
    for row in range(3):
        for column in range(4):
            if matrix[row][column] == matrix[row + 1][column]:
                return True
    return False

def gameOver(matrix):
    if any(2048 in row for row in matrix):
        print('You win!')
        return True
    elif not any(0 in row for row in matrix) and not horizontalMoveExists(matrix) and not verticalMoveExists(matrix):
        print('You lost!')
        return True
    else:
        return False

#####

# noodle = row/column
def mergeNoodle(n1,n2,n3,n4):
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
    newMatrix = newTile(newMatrix)
    gameOver(newMatrix)
    return newMatrix

def up(matrix):
    newMatrix = [[],[],[],[]]
    for row in range(4):
        noodle = mergeNoodle(matrix[0][row],matrix[1][row],matrix[2][row],matrix[3][row])
        for j in range(4):
            newMatrix[j] += [noodle[j]]
    newMatrix = newTile(newMatrix)
    gameOver(newMatrix)
    return newMatrix

def left(matrix):
    newMatrix = []
    for row in range(4):
        newMatrix += [mergeNoodle(matrix[row][0],matrix[row][1],matrix[row][2],matrix[row][3])]
    newMatrix = newTile(newMatrix)
    gameOver(newMatrix)
    return newMatrix

def right(matrix):
    newMatrix = []
    for row in range(4):
        newNoodle = [mergeNoodle(matrix[row][3],matrix[row][2],matrix[row][1],matrix[row][0])]
        newMatrix += [newNoodle[0][::-1]]
    newMatrix = newTile(newMatrix)
    gameOver(newMatrix)
    return newMatrix

matrix = newGame()
print('Stiskni jedno z tlacitek W↑,A←,S↓,D→ pro pohyb v poli.')
printBoard(matrix)

while not gameOver(matrix):
    smer = input('Pohyb: ').lower()
    if smer == 'w':
        matrix = up(matrix)
    elif smer == 'a':
        matrix = left(matrix)
    elif smer == 's':
        matrix = down(matrix)
    elif smer == 'd':
        matrix = right(matrix)
    else:
        print('Spatne tlacitko, opakuj znovu. (W↑,A←,S↓,D→)')

    printBoard(matrix)


'''matrix = [[2, 0, 16, 2], [0, 0, 16, 2], [2, 4, 0, 0], [2, 4, 16, 0]]

root = tk.Tk()
root.title('2048')
root.geometry('600x400+300+150')
#makeGUI(root)

root.mainloop()'''