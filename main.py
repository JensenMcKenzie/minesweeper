from tkinter import *
import random

window = Tk()
window.geometry("480x660")
window.title("Minesweeper")

flagStatus = False
gameOver = False
isCheating = False

bombAmount = 20
slider = Scale()
done = []
bombs = []

board = [[-1 for i in range(20)] for j in range(20)]
boardTwo = [[0 for i in range(20)] for j in range(20)]
boardDone = [[0 for i in range(20)] for j in range(20)]


def sliderchange(s):
    global bombAmount, slider
    bombAmount = slider.get()


def cheat():
    global board, bombs, isCheating
    isCheating = True
    for i in range(20):
        for j in range(20):
            if board[i][j] in bombs:
                board[i][j].configure(bg='red')
            elif boardDone[i][j] != 1:
                board[i][j].configure(bg='green')


def flagtoggle():
    global flagStatus
    flagStatus = not flagStatus
    if not flagStatus:
        flag.configure(relief='raised')
    else:
        flag.configure(relief='sunken')


def generatebombs():
    global bombs, boardTwo, isCheating
    boardTwo = [[0 for i in range(20)] for j in range(20)]
    bombs = []
    while len(bombs) < bombAmount:
        row = random.choice(range(20))
        column = random.choice(range(20))
        b = board[row][column]
        if b not in bombs:
            for horizontal in range(-1, 2):
                for vertical in range(-1, 2):
                    if not (horizontal == 0 and vertical == 0):
                        if 0 <= b.grid_info()["row"] + vertical <= 19 and \
                                b.grid_info()["column"] + horizontal >= 0 and b.grid_info()[
                                "column"] + horizontal <= 19:
                            x = board[b.grid_info()["row"] + vertical][b.grid_info()["column"] + horizontal]
                            if x not in bombs:
                                boardTwo[b.grid_info()["row"] + vertical][b.grid_info()["column"] + horizontal] += 1
            bombs.append(b)
            boardTwo[row][column] = -1
    if isCheating:
        cheat()


def buttonpress(b):
    global flagStatus, done, gameOver
    if gameOver:
        return
    x = b.grid_info()['row']
    y = b.grid_info()['column']
    if len(done) == 0 and boardTwo[x][y]:
        while boardTwo[x][y] != 0:
            generatebombs()
    if flagStatus:
        if b.cget('bg') == 'blue':
            b.configure(bg='#f0f0f0')
        else:
            b.configure(bg='blue')
    else:
        queue = []
        if boardTwo[x][y] == 0:
            done.append(b)
            boardDone[x][y] = 1
            queue.append(b)
            b.configure(text=boardTwo[x][y], bg='#f0f0f0', state=DISABLED)
            while not len(queue) == 0:
                b = queue.pop(0)
                x = b.grid_info()['row']
                y = b.grid_info()['column']
                if x - 1 >= 0:
                    if boardDone[x - 1][y] != 1 and boardTwo[x][y] == 0:
                        queue.append(board[x - 1][y])
                        done.append(board[x - 1][y])
                        boardDone[x - 1][y] = 1
                        board[x - 1][y].configure(text=boardTwo[x - 1][y], bg='orange', state=DISABLED) if \
                            boardTwo[x - 1][y] != 0 else board[x - 1][y].configure(text=boardTwo[x - 1][y],
                                                                                   bg='#f0f0f0',
                                                                                   state=DISABLED)
                if x + 1 <= 19:
                    if boardDone[x + 1][y] != 1 and boardTwo[x][y] == 0:
                        queue.append(board[x + 1][y])
                        done.append(board[x + 1][y])
                        boardDone[x + 1][y] = 1
                        board[x + 1][y].configure(text=boardTwo[x + 1][y], bg='orange', state=DISABLED) if \
                            boardTwo[x + 1][y] != 0 else board[x + 1][y].configure(text=boardTwo[x + 1][y],
                                                                                   bg='#f0f0f0',
                                                                                   state=DISABLED)
                if y - 1 >= 0:
                    if boardDone[x][y - 1] != 1 and boardTwo[x][y] == 0:
                        queue.append(board[x][y - 1])
                        done.append(board[x][y - 1])
                        boardDone[x][y - 1] = 1
                        board[x][y - 1].configure(text=boardTwo[x][y - 1], bg='orange', state=DISABLED) if boardTwo[x][
                                                                                                               y - 1] != 0 else \
                            board[x][y - 1].configure(text=boardTwo[x][y - 1], bg='#f0f0f0', state=DISABLED)
                if y + 1 <= 19:
                    if boardDone[x][y + 1] != 1 and boardTwo[x][y] == 0:
                        queue.append(board[x][y + 1])
                        done.append(board[x][y + 1])
                        boardDone[x][y + 1] = 1
                        board[x][y + 1].configure(text=boardTwo[x][y + 1], bg='orange', state=DISABLED) if boardTwo[x][
                                                                                                               y + 1] != 0 else \
                            board[x][y + 1].configure(text=boardTwo[x][y + 1], bg='#f0f0f0', state=DISABLED)

        elif boardTwo[x][y] == -1:
            for i in range(0, 20):
                for j in range(0, 20):
                    board[i][j].configure(text='', bg='red', state=DISABLED)
            gameOver = True
        else:
            if b.cget('text') == '':
                x = b.grid_info()['row']
                y = b.grid_info()['column']
                b.configure(text=boardTwo[x][y], bg='orange', state=DISABLED)
                done.append(b)
                boardDone[x][y] = 1
    if len(done) == 400 - bombAmount:
        for i in range(0, 20):
            for j in range(0, 20):
                board[i][j].configure(text='', bg='green', state=DISABLED)
        gameOver = True


def generategrid():
    global board, done, gameOver, boardDone, isCheating
    isCheating = False
    gameOver = False
    done = []
    boardDone = [[0 for i in range(20)] for j in range(20)]
    for i in range(20):
        for j in range(20):
            if type(board[i][j]) == Button:
                board[i][j].configure(text='', bg='#f0f0f0', state=NORMAL)
                continue
            b = Button(text='', width=2, height=1, bg='#f0f0f0')
            b.configure(command=lambda button=b: buttonpress(button))
            b.grid(row=i, column=j)
            board[i][j] = b
    generatebombs()


generategrid()

flag = Button(text="Flag", width=10, height=3, command=flagtoggle)
flag.place(x=360, y=550)
cheatButton = Button(text="Cheat", width=10, height=3, command=cheat)
cheatButton.place(x=30, y=550)
slider = Scale(from_=10, to=50, length=350, orient=HORIZONTAL, command=sliderchange)
slider.set(20)
slider.place(x=100, y=610)
label = Label(text='Bombs:')
label.place(x=30, y=625)
x = Button(text="Reset", width=20, height=3, command=generategrid)
x.place(x=160, y=550)
window.mainloop()
