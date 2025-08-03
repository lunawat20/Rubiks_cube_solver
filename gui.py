# gui.py - Tkinter GUI

import tkinter as tk
from cube import create_solved_cube, rotate_face
from solver import solve

FACE_COLORS = {
    'U': 'white', 'D': 'yellow',
    'F': 'green', 'B': 'blue',
    'L': 'orange', 'R': 'red'
}

class CubeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("3x3 Rubik's Cube Solver")
        self.canvas = tk.Canvas(root, width=400, height=300)
        self.canvas.pack()
        self.cube = create_solved_cube()
        self.draw_cube()

        control_frame = tk.Frame(root)
        control_frame.pack()

        tk.Button(control_frame, text="Scramble", command=self.scramble).pack(side=tk.LEFT)
        tk.Button(control_frame, text="Solve", command=self.solve).pack(side=tk.LEFT)

    def draw_face(self, face_matrix, top_left_x, top_left_y, size=30):
        for i in range(3):
            for j in range(3):
                color = face_matrix[i][j]
                x1 = top_left_x + j * size
                y1 = top_left_y + i * size
                x2 = x1 + size
                y2 = y1 + size
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline='black')

    def draw_cube(self):
        self.canvas.delete("all")
        offset = 100
        self.draw_face(self.cube['U'], offset + 90, 10)
        self.draw_face(self.cube['L'], offset, 100)
        self.draw_face(self.cube['F'], offset + 90, 100)
        self.draw_face(self.cube['R'], offset + 180, 100)
        self.draw_face(self.cube['B'], offset + 270, 100)
        self.draw_face(self.cube['D'], offset + 90, 190)

    def scramble(self):
        import random
        moves = ['R', "R'", 'U', "U'", 'F', "F'"]
        self.scramble_moves = [random.choice(moves) for _ in range(10)]
        print("Scrambled with:", self.scramble_moves)
        # Not implementing full scramble effect on cube for now

    def solve(self):
        steps = solve(self.cube)
        print("Solving steps:", steps)
        # Not animating steps for now

