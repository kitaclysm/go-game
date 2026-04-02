import tkinter as tk
from tkinter import *
from node_space import SpaceType, SpaceNode

grid_size = 30
canvas_size = 600

root = tk.Tk()

# create window
root.title("Go")
root.configure(background="green")
root.minsize(800, 800)
root.maxsize(1200,1200)
root.geometry("800x800+50+50")

# create board centered in window
canvas = Canvas(root, width=canvas_size, height=canvas_size)
canvas.place(relx=0.5, rely=0.5, anchor='center')
# add grid lines
for i in range(1, 20):
	imult = grid_size*i
	# horizontal
	canvas.create_line(grid_size, imult, (canvas_size - grid_size), imult)
	# vertical
	canvas.create_line(imult, grid_size, imult, (canvas_size - grid_size))

# create space_nodes
spaces = [[None for c in range(19)] for r in range(19)]
for r in range(19):
    for c in range(19):
        spaces[r][c] = SpaceNode(row=r, col=c)

# create chip indicator and hide
chip_hoverer = canvas.create_oval(0,0,((grid_size / 2) - 4),((grid_size / 2) - 4))
# alternate chip indicator, rounded circle instead of oval
# chip_hoverer = canvas.create_polygon([2, 0, 8, 0, 10, 2, 10, 8, 8, 10, 2, 10, 0, 8, 0, 2], smooth=True)
canvas.itemconfig(chip_hoverer, state='hidden')

def show_chip_placer(event):
    canvas.itemconfig(chip_hoverer, state='normal')

def hide_chip_placer(event):
    canvas.itemconfig(chip_hoverer, state='hidden')

def handle_motion(event):
    if event.x < 15 or event.x > 585 or event.y < 15 or event.y > 585:
        hide_chip_placer(event)
    else:
        show_chip_placer(event)
    snapped_x = ((event.x + (grid_size / 2)) // grid_size) * grid_size
    x1 = snapped_x - ((grid_size / 2) - 4)
    x2 = snapped_x + ((grid_size / 2) - 4)
    snapped_y = ((event.y + (grid_size / 2)) // grid_size) * grid_size
    y1 = snapped_y - ((grid_size / 2) - 4)
    y2 = snapped_y + ((grid_size / 2) - 4)
    canvas.coords(chip_hoverer, x1, y1, x2, y2)
    # print(f"snapped_x: {snapped_x}, snapped_y: {snapped_y}")

def handle_click(event):
	col = event.x
	row = event.y
	print(f"Clicked at {event.x}, {event.y}")

canvas.bind('<Button-1>', handle_click)
# canvas.bind('<Enter>', show_chip_placer)
canvas.bind('<Leave>', hide_chip_placer)
canvas.bind('<Motion>', handle_motion)