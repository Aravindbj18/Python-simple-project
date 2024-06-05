import random

class Food:
    def __init__(self,  board_size,cell_size):

        self.x = random.randrange(0, 400, 10)
        self.y = random.randrange(0, 400, 10)
        self.board_size = board_size
        self.cell_size = cell_size

    def spawn(self):  
        
        self.x = random.randrange(0, 400, 10)
        self.y = random.randrange(0, 400, 10)
        