import pygame 

from pieces import Piece

class Game:
    
    def __init__(self, screen) -> None:
        self.screen = screen
        self.score = None 
        self.is_over = True 
        self.current_piece = None 
        self.grid = None 
        self.grid_colors = None 
        
    # Reset.
    def reset(self):
        self.is_over = False
        self.score = 0.0
        self.grid = [[0.0] * 10 for i in range (20)]
        self.grid_colors = [[None] * 10 for i in range (20)]
        self.current_piece = Piece()
    
    # Move left.
    def move_left(self):
        pass 
    
    # Move right. 
    def move_right(self):
        pass 
    
    # Move down.
    def move_down(self): 
        pass
        
    # Rotate.
    def rotate(self):
        pass
        
    # Update. 
    def update(self):
        pass
    
    # Render. 
    def render(self):
        pass
    
    