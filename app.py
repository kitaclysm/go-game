import tkinter as tk
from tkinter import *

root = tk.Tk()

root.title("Go")
root.configure(background="green")
root.minsize(800, 800)
root.maxsize(1200,1200)
root.geometry("800x800+50+50")

canvas = Canvas(root, width=600, height=600)
canvas.place(relx=0.5, rely=0.5, anchor='center')

x_coords = []
y_coords = []

for i in range(1, 20):
	imult = 30*i
	# horizontal
	canvas.create_line(30, imult, 570, imult)
	# vertical
	canvas.create_line(imult, 30, imult, 570)
	
	x_coords.extend([imult])
	y_coords.extend([imult])

coords = [x_coords, y_coords]
print(coords)

def handle_click(event):
	col = event.x
	row = event.y
	print(f"Clicked at {event.x}, {event.y}")

canvas.bind("<Button-1>", handle_click)

root.mainloop()