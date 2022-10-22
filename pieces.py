from random import choice

GEOMETRY = [
    [[0, 0], [-1, 0], [-1, 1], [0, 1]],      # Square Piece
    [[0, 0], [0, -1], [0, 1], [0, 2]],       # Bar Piece
    [[0, 0], [0, -1], [0, 1], [1, 0]],       # T-Shaped Piece
    [[0, 0], [0, 1], [0, -1], [-1, -1]],     # Left L Piece
    [[0, 0], [0, -1], [0, 1], [-1, 1]],      # Right L Piece
    [[0, 0], [-1, -1], [-1, 0], [0, 1]],     # Left S Piece
    [[0, 0], [-1, 0], [0, -1], [-1, 1]]      # Right S Piece
]

COLOR = [
    (0, 238, 238),   # Clear Blue
    (23, 1, 232),    # Dark Blue
    (0, 238, 33),    # Green
    (153, 0, 239),   # Purple
    (238, 0, 20),    # Red
    (237, 238, 42),  # Yellow
    (255, 215, 0)    # Orange
]

class Piece:
    
    def __init__(self) -> None:
        self.center_row = 0
        self.center_col = 4
        self.relative_coords = choice(GEOMETRY)
        self.color = choice(COLOR)
    
    @property
    def global_coords(self):
        return [[row + self.center_row, col + self.center_col]
            for row, col in self.relative_coords]