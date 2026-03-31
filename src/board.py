import tkinter as tk
from tkinter import *

grid_size = 30
canvas_size = 600

root = tk.Tk()

root.title("Go")
root.configure(background="green")
root.minsize(800, 800)
root.maxsize(1200,1200)
root.geometry("800x800+50+50")

canvas = Canvas(root, width=canvas_size, height=canvas_size)
canvas.place(relx=0.5, rely=0.5, anchor='center')

def round_rectangle(x1, y1, x2, y2, radius=2, **kwargs):
    points = [
        x1+radius, y1,
        x1+radius, y1,
        x2-radius, y1,
        x2-radius, y1,
        x2, y1,
        x2, y1+radius,
        x2, y1+radius,
        x2, y2-radius,
        x2, y2-radius,
        x2, y2,
        x2-radius, y2,
        x2-radius, y2,
        x1+radius, y2,
        x1+radius, y2,
        x1, y2,
        x1, y2-radius,
        x1, y2-radius,
        x1, y1+radius,
        x1, y1+radius,
        x1, y1
    ]
    return canvas.create_polygon(points, **kwargs, smooth=True)

for i in range(1, 20):
	imult = grid_size*i
	# horizontal
	canvas.create_line(grid_size, imult, (canvas_size - grid_size), imult)
	# vertical
	canvas.create_line(imult, grid_size, imult, (canvas_size - grid_size))

def create_hoverer(event):
    snapped_x = ((event.x + (grid_size / 2)) // grid_size) * grid_size
    x1 = snapped_x - ((grid_size / 2) - 4)
    x2 = snapped_x + ((grid_size / 2) - 4)
    snapped_y = ((event.y + (grid_size / 2)) // grid_size) * grid_size
    y1 = snapped_y - ((grid_size / 2) - 4)
    y2 = snapped_y + ((grid_size / 2) - 4)
    # hoverer = round_rectangle(x1, y1, x2, y2, fill='yellow')
    hoverer = canvas.create_oval(x1, y1, x2, y2, fill ='yellow')

def handle_hover(event):
    canvas.coords(hoverer, x1, y1, x2, y2)
    print(f"snapped_x: {snapped_x}, snapped_y: {snapped_y}")

def handle_click(event):
	col = event.x
	row = event.y
	print(f"Clicked at {event.x}, {event.y}")

canvas.bind('<Button-1>', handle_click)
canvas.bind('<Enter>', create_hoverer)
canvas.bind('<Motion>', handle_hover)