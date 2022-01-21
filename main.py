import random
import tkinter as tk
from tkinter import messagebox

# theme from https://flatuicolors.com
colors = {
    '': '#bdc3c7',
    2: '#1abc9c',
    4: '#16a085',
    8: '#2ecc71',
    16: '#27ae60',
    32: '#3498db',
    64: '#2980b9',
    128: '#9b59b6',
    256: '#8e44ad',
    512: '#f1c40f',
    1024: '#f39c12',
    2048: '#e67e22'
}

def newTile(matrix):
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
        # 90% chance of the new number being a 2; 10% chance of a 4 (for more authentic experience)
        chance = random.randint(0,9)
        if chance < 1:
            matrix[row][column] = 4
        else:
            matrix[row][column] = 2
    else:
        newTile(matrix)
    return matrix

def newGame():
    matrix = [[0] * 4 for _ in range(4)]
    newTile(matrix)
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
    global root
    if any(2048 in row for row in matrix):
        messagebox.showinfo('2048', 'You\'ve won!')
        root.destroy()
    elif not any(0 in row for row in matrix) and not horizontalMoveExists(matrix) and not verticalMoveExists(matrix):
        messagebox.showinfo('2048', 'You\'ve lost!')
        root.destroy()

#####

# noodle = row/column
def mergeNoodle(n1,n2,n3,n4):
    '''
    Function that takes 4 numbers from one row/col and does a slide to n1 (with merging). 
    '''
    
    # slide to n1 without merging (firstly I need nonzero numbers as close as possible to n1)
    noodle = [n1, n2, n3, n4]
    newNoodle = []
    counter = 4
    for num in noodle:
        if num != 0:
            newNoodle.append(num)
            counter -= 1
    nulls = [0] * counter
    noodle = newNoodle + nulls
    
    # now merging nonzero numbers (from n1)
    if noodle[0] == noodle[1]: 
        noodle[0] *= 2
        noodle[1] = 0
    if noodle[1] == noodle[2]: 
        noodle[1] *= 2
        noodle[2] = 0
    if noodle[2] == noodle[3]: 
        noodle[2] *= 2
        noodle[3] = 0

    # another slide to n1 (zeros may occur after merge between nonzero nums)
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
    for col in range(4):
        noodle = [mergeNoodle(matrix[3][col],matrix[2][col],matrix[1][col],matrix[0][col])][0][::-1]
        for j in range(4):
            newMatrix[j] += [noodle[j]]
    newMatrix = newTile(newMatrix)
    return newMatrix

def up(matrix):
    newMatrix = [[],[],[],[]]
    for col in range(4):
        noodle = mergeNoodle(matrix[0][col],matrix[1][col],matrix[2][col],matrix[3][col])
        for j in range(4):
            newMatrix[j] += [noodle[j]]
    newMatrix = newTile(newMatrix)
    return newMatrix

def left(matrix):
    newMatrix = []
    for row in range(4):
        newMatrix += [mergeNoodle(matrix[row][0],matrix[row][1],matrix[row][2],matrix[row][3])]
    newMatrix = newTile(newMatrix)
    return newMatrix

def right(matrix):
    newMatrix = []
    for row in range(4):
        newNoodle = [mergeNoodle(matrix[row][3],matrix[row][2],matrix[row][1],matrix[row][0])]
        newMatrix += [newNoodle[0][::-1]]
    newMatrix = newTile(newMatrix)
    return newMatrix

def updateGUI(matrix):
    global labels
    for row in range(4):
        for col in range(4):
            num = matrix[row][col]
            if num == 0:
                num = ''
            labels[row][col].configure(bg=colors[num], text=str(num))

root = tk.Tk()
root.title('2048')
root.geometry('400x370')
root.resizable(False, False)

messagebox.showinfo("Info","Press -arrow keys- or -w,a,s,d keys- to play the game.")

labels = [[None] * 4 for _ in range(4)]

for row in range(4):
    for col in range(4):
        labels[row][col] = tk.Label(root, bg='#bdc3c7', text='', font='Arial 18', fg='white', width=7, height=3)
        labels[row][col].grid(column=col, row=row, padx=2, pady=2)

matrix = newGame()
updateGUI(matrix)

def move(event):
    global matrix
    if event.char == 'w' or event.keysym == 'Up':
        matrix = up(matrix)
    elif event.char == 'a' or event.keysym == 'Left':
        matrix = left(matrix)
    elif event.char == 's' or event.keysym == 'Down':
        matrix = down(matrix)
    elif event.char == 'd' or event.keysym == 'Right':
        matrix = right(matrix)

    updateGUI(matrix)
    gameOver(matrix)

    if event.keysym == 'Escape':
        root.destroy()

root.bind('<Key>', move)

root.mainloop()
