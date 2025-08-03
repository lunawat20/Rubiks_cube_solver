# cube.py - Cube model and move engine

FACE_COLORS = {
    'U': 'white',
    'D': 'yellow',
    'F': 'green',
    'B': 'blue',
    'L': 'orange',
    'R': 'red'
}

def create_solved_cube():
    return {
        face: [[FACE_COLORS[face]] * 3 for _ in range(3)]
        for face in 'UDFBLR'
    }

def rotate_face(face):
    return [list(reversed(col)) for col in zip(*face)]
