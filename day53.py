"""
This module allows users to draw on a canvas using a GUI.
"""

import pickle
import tkinter as tk


class DrawingApp:
    """
    A class to represent a drawing application.
    """

    def __init__(self, root: tk.Tk) -> None:
        """
        Initialize the DrawingApp with a root widget.

        Args:
            root (tk.Tk): The root widget of the application.
        """
        self.canvas = tk.Canvas(root, width=600, height=400, bg="white")
        self.canvas.pack(side="top", fill="both", expand=True)
        self.canvas.bind("<Button-1>", self.draw_shape)
        self.canvas.bind("<Button-3>", self.erase_shape)
        self.color = "black"
        self.draw_mode = "circle"
        self.shapes = []

        # Create color selection menu
        self.color_var = tk.StringVar(root)
        self.color_var.set(self.color)
        self.color_menu = tk.OptionMenu(
            root, self.color_var, "black", "red", "green", "blue", "yellow", "purple"
        )
        self.color_menu.pack(side="top")
        self.color_var.trace_add("write", self.change_color)

        # Create draw mode menu
        self.draw_mode_var = tk.StringVar(root)
        self.draw_mode_var.set(self.draw_mode)
        self.draw_mode_menu = tk.OptionMenu(root, self.draw_mode_var, "circle", "line")
        self.draw_mode_menu.pack(side="top")
        self.draw_mode_var.trace_add("write", self.change_draw_mode)

    def draw_shape(self, event):
        """
        Draw a shape on the canvas at the event location.

        Args:
            event: The event that triggered this method.
        """
        x, y = event.x, event.y
        if self.draw_mode == "circle":
            radius = 10
            self.canvas.create_oval(
                x - radius, y - radius, x + radius, y + radius, fill=self.color
            )
        elif self.draw_mode == "line":
            self.canvas.create_line(x, y, x, y, fill=self.color, width=2)

    def erase_shape(self, event):
        """
        Erase a shape on the canvas at the event location.

        Args:
            event: The event that triggered this method.
        """
        x, y = event.x, event.y
        self.canvas.delete(self.canvas.find_closest(x, y))

    def change_color(self, *args):
        """
        Change the color of the shapes to be drawn.
        """
        self.color = self.color_var.get()

    def change_draw_mode(self, *args):
        """
        Change the drawing mode.
        """
        self.draw_mode = self.draw_mode_var.get()

    def save_drawing(self, filename):
        """
        Save the current drawing to a file.

        Args:
            filename (str): The name of the file to save to.
        """
        with open(filename, "w", encoding="utf-8") as f:
            for shape in self.shapes:
                f.write(f"{shape}\n")

    def load_drawing(self, filename):
        """
        Load a drawing from a file.

        Args:
            filename (str): The name of the file to load from.
        """
        with open(filename, "r", encoding="utf-8") as f:
            self.canvas.delete("all")
            self.shapes = []
            for line in f:
                shape = line.strip()
                self.shapes.append(shape)
            self.redraw_shapes()

    def redraw_shapes(self):
        """
        Redraw shapes on the canvas.
        """
        # Implement this method to redraw shapes on the canvas based on the self.shapes list

        for shape in self.shapes:
            shape_type, *coords = shape.split()
            if shape_type == "oval":
                self.canvas.create_oval(*coords, fill=self.color)
            elif shape_type == "line":
                self.canvas.create_line(*coords, fill=self.color, width=2)


main_root = tk.Tk()
app = DrawingApp(main_root)
main_root.mainloop()
