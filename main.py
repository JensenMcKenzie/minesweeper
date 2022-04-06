from tkinter import *
import random

window = Tk()
window.geometry("480x650")
rows = 20
columns = 20
flag = False
done = []

board = [[-1 for i in range(20)] for j in range(20)]
boardTwo = [[0 for i in range(0, 20)] for j in range(0, 20)]


def flagtoggle():
    global flag
    flag = not flag


def buttonPress(b):
    global flag, done
    print(len(done))
    x = b.grid_info()['row']
    y = b.grid_info()['column']
    if not flag:
        if b.cget('bg') == 'blue':
            b.configure(bg='#f0f0f0')
        else:
            b.configure(bg='blue')
    else:
        queue = []
        if boardTwo[x][y] == 0:
            queue.append(b)
            b.configure(text=boardTwo[x][y])
            while not len(queue) == 0:
                b = queue.pop(0)
                x = b.grid_info()['row']
                y = b.grid_info()['column']
                if x - 1 >= 0:
                    if board[x - 1][y] not in done and boardTwo[x][y] == 0:
                        queue.append(board[x - 1][y])
                        done.append(board[x - 1][y])
                        if boardTwo[x - 1][y] != 0:
                            board[x - 1][y].configure(text=boardTwo[x - 1][y], bg='red')
                        else:
                            board[x - 1][y].configure(text=boardTwo[x - 1][y])
                if x + 1 <= 19:
                    if board[x + 1][y] not in done and boardTwo[x][y] == 0:
                        queue.append(board[x + 1][y])
                        done.append(board[x + 1][y])
                        if boardTwo[x + 1][y] != 0:
                            board[x + 1][y].configure(text=boardTwo[x + 1][y], bg='red')
                        else:
                            board[x + 1][y].configure(text=boardTwo[x + 1][y])
                if y - 1 >= 0:
                    if board[x][y - 1] not in done and boardTwo[x][y] == 0:
                        queue.append(board[x][y - 1])
                        done.append(board[x][y - 1])
                        if boardTwo[x][y - 1] != 0:
                            board[x][y - 1].configure(text=boardTwo[x][y - 1], bg='red')
                        else:
                            board[x][y - 1].configure(text=boardTwo[x][y - 1])
                if y + 1 <= 19:
                    if board[x][y + 1] not in done and boardTwo[x][y] == 0:
                        queue.append(board[x][y + 1])
                        done.append(board[x][y + 1])
                        if boardTwo[x][y + 1] != 0:
                            board[x][y + 1].configure(text=boardTwo[x][y + 1], bg='red')
                        else:
                            board[x][y + 1].configure(text=boardTwo[x][y + 1])
        elif boardTwo[x][y] == -1:
            for i in range(0, 20):
                for j in range(0, 20):
                    board[i][j].configure(text='', bg='red')
        else:
            if b not in done:
                x = b.grid_info()['row']
                y = b.grid_info()['column']
                b.configure(text=boardTwo[x][y], bg='red')
                done.append(b)
    if len(done) == 380:
        for i in range(0, 20):
            for j in range(0, 20):
                board[i][j].configure(text='', bg='green')


def generateGrid():
    global boardTwo, board, done
    done = []
    boardTwo = [[0 for i in range(0, 20)] for j in range(0, 20)]
    board = [[0 for i in range(0, 20)] for j in range(0, 20)]
    for i in range(0, rows):
        for j in range(0, columns):
            b = Button(text='', width=2, height=1)
            b.configure(command=lambda button=b: buttonPress(button))
            b.grid(row=i, column=j)
            board[i][j] = b
    bombs = []
    while len(bombs) < 20:
        row = random.randint(0, 19)
        column = random.randint(0, 19)
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


flag = Button(text="Flag Toggle", width=10, height=3, command=flagtoggle)
flag.place(x=360, y=550)
cheat = Button(text="Cheat", width=10, height=3)
cheat.place(x=30, y=550)
x = Button(text="Start", width=20, height=3, command=generateGrid)
x.place(x=160, y=550)
window.mainloop()
