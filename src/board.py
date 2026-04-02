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

# create space_nodes and grid lines
spaces = [[None for c in range(19)] for r in range(19)]
for r in range(19):
    for c in range(19):
        spaces[r][c] = SpaceNode(row=r, col=c)
    # horizontal
    canvas.create_line(grid_size, grid_size * (r + 1), canvas_size - grid_size, grid_size * (r + 1), fill='red')
    # vertical
    canvas.create_line(grid_size * (r + 1), grid_size, grid_size * (r + 1), canvas_size - grid_size, fill='green')

# create chip indicator and hide
chip_hoverer = canvas.create_oval(0,0,((grid_size / 2) - 4),((grid_size / 2) - 4), fill='pink')
# alternate chip indicator, rounded circle instead of oval
# chip_hoverer = canvas.create_polygon([2, 0, 8, 0, 10, 2, 10, 8, 8, 10, 2, 10, 0, 8, 0, 2], smooth=True)
canvas.itemconfig(chip_hoverer, state='hidden')

def show_chip_placer(event):
    canvas.itemconfig(chip_hoverer, state='normal')

def hide_chip_placer(event):
    canvas.itemconfig(chip_hoverer, state='hidden')

def handle_motion(event):
    # if statements prevent hoverer from snapping to spaces outside the grid
    if event.x < 30:
        snapped_x = 30
    elif event.x > 570:
        snapped_x = 570
    else:
        snapped_x = ((event.x + (grid_size / 2)) // grid_size) * grid_size
    if event.y < 30:
        snapped_y = 30
    elif event.y > 570:
        snapped_y = 570
    else:
        snapped_y = ((event.y + (grid_size / 2)) // grid_size) * grid_size
    show_chip_placer(event)
    x1 = snapped_x - ((grid_size / 2) - 4)
    x2 = snapped_x + ((grid_size / 2) - 4)
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