from cgitb import text
from ctypes import alignment
from platform import win32_edition
from tkinter import *
import tkinter as tk
from tkinter.simpledialog import SimpleDialog
import ctypes
from PIL import Image, ImageTk

from pip import main

N=9

def instruct():
    instuctWindow=tk.Toplevel()
    instuctWindow.geometry("600x100")
    instuctWindow.title("Instructiuni")
    icon2=Image.open("sudoku.png")
    photo2=ImageTk.PhotoImage(icon2)
    instuctWindow.wm_iconphoto(False,photo2)
    instuctWindow.resizable(0,0)
    label1 = tk.Label(instuctWindow, text="Inlocuiti zerourile cu cifrele din sudoku-ul pe care il aveti de rezolvat apoi apasati rezolvat",font=("Helvetica",10))
    label1.pack()
    label2 = tk.Label(instuctWindow, text="Atentie: programul nu va rula daca introduceti un sudoku invalid", font=("Helvetica",10))
    label2.pack()
    label3 = tk.Label(instuctWindow, text="Exemplu: Doua cifre identice se afla una langa alta, acest caz ducand la blocarea programului", font=("Helvetica",10))
    label3.pack()
def refresh(self):
    self.destroy()
    window=tk.Tk()
    window.geometry("500x600")
    window.title("Sudoku")
    icon=Image.open('sudoku.png')
    photo=ImageTk.PhotoImage(icon)
    window.wm_iconphoto(False,photo)
    for i in range(9):
        for j in range(9):
         m[i][j]=tk.Text(window, width=3, height=1.5, font=("Helvetica",16))
         m[i][j].insert('end',0)
         m[i][j].grid(row=i, column=j, sticky=tk.W+tk.E)
    submit_button=tk.Button(window, text="Rezolva",width=10, height=2, command=lambda: submit())
    submit_button.place(x=160, y=470)
    submit_button=tk.Button(window, text="Restart",width=10, height=2, command=lambda: refresh(window))
    submit_button.place(x=80, y=470)
    window.resizable(0,0)
    submit_button=tk.Button(window, text="Instructiuni",width=10, height=2, command=lambda: instruct())
    submit_button.place(x=1, y=470)



def printing(array):
    for i in range(N):
        for j in range(N):
            print(array[i][j], end= " ")
        print()
        
def ok(grid, row, col, number):
    for x in range(9):
        if grid[row][x]==number:
            return False
    for x in range(9):
        if grid[x][col]==number:
            return False
    startRow=row-row%3
    startCol=col-col%3
    for i in range(3):
        for j in range(3):
            if grid[i+startRow][j+startCol]==number:
                return False
    return True

def BT(grid,row,col):
    if (row==N-1 and col==N):
        return True
    if col==N:
        row=row+1
        col=0
    if grid[row][col]>0:
        return BT(grid,row,col+1)
    for number in range(1,N+1,1):
        if ok(grid,row,col,number):
            grid[row][col]=number
            if BT(grid,row,col+1):  
                return True
        grid[row][col]=0
    return False

def submit():
    for i in range(9):
        for j in range(9):
                b[i][j]=m[i][j].get("1.0",'end-1c')
                try:
                    int(float(b[i][j]))
                except ValueError:
                    print("Sudoku Invalid")
                    ctypes.windll.user32.MessageBoxW(0, "Sudoku Invalid", "Eroare", 1)
                    quit()
                b[i][j]=int(float(b[i][j]))
                if b[i][j]/10>=1:
                    print("Sudoku Invalid")
                    ctypes.windll.user32.MessageBoxW(0, "Sudoku Invalid", "Eroare", 1)
                    quit()
    if (BT(b,0,0)):
        newWindow=tk.Toplevel()
        newWindow.geometry("500x600")
        newWindow.title("Solutie")
        icon2=Image.open("sudoku.png")
        photo2=ImageTk.PhotoImage(icon2)
        newWindow.wm_iconphoto(False,photo2)
        newWindow.resizable(0,0)
        for i in range(9):
            for j in range(9):
                s[i][j]=tk.Text(newWindow,width=3, height=1.5, font=("Helvetica",16))
                s[i][j].insert(tk.INSERT,b[i][j])
                s[i][j].grid(row=i, column=j, sticky=tk.W+tk.E)
    else:
        print("Nu are solutii")
        
window=tk.Tk()
window.geometry("500x600")
window.title("Sudoku")
icon=Image.open('sudoku.png')
photo=ImageTk.PhotoImage(icon)
window.wm_iconphoto(False,photo)
window.resizable(0,0)

s=[[0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0]]
m=[[0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0]]
b=[[0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0]]

for i in range(9):
    for j in range(9):
        m[i][j]=tk.Text(window, width=3, height=1.5, font=("Helvetica",16))
        m[i][j].insert('end',0)
        m[i][j].grid(row=i, column=j, sticky=tk.W+tk.E)

submit_button=tk.Button(window, text="Rezolva",width=10, height=2, command=lambda: submit())
submit_button.place(x=160, y=470)

submit_button=tk.Button(window, text="Restart",width=10, height=2, command=lambda: refresh(window))
submit_button.place(x=80, y=470)

submit_button=tk.Button(window, text="Instructiuni",width=10, height=2, command=lambda: instruct())
submit_button.place(x=1, y=470)


window.mainloop()