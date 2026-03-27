import tkinter as tk
from tkinter import *

root = tk.Tk()

root.title("Go")
root.configure(background="green")
root.minsize(800, 800)
root.maxsize(1200,1200)
root.geometry("800x800+50+50")

canvas = Canvas(root, width=600, height=600)
canvas.pack()

for i in range(20):
    imult = 30*i
    # horizontal, x_start is 0, x_end is 600, y_start and y_end is 3 * i
    canvas.create_line(0, imult, 600, imult)
    # vertical, inverse of horizontal
    canvas.create_line(imult, 0, imult, 600)


root.mainloop()