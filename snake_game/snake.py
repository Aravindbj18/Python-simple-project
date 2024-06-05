DIRECTION = {'RIGHT': [1, 0],
             'LEFT': [-1, 0],
             'UP':[0, -1],
             'DOWN': [0, 1]}


class Snake:
    def __init__(self,x ,y, board_size, cell_size, speed, direction):
        self.blocks =[[x, y]]
        self.board_size = board_size
        self.cell_size = cell_size
        self.speed = speed
        self.direction = direction
        self.length =1

    def update_position(self):
        head_x = (self.blocks[0][0] + DIRECTION[self.direction][0] * self.speed ) % self.board_size
        head_y = (self.blocks[0][1] + DIRECTION[self.direction][1] * self.speed ) % self.board_size
        for i in range(self.length-1):
            self.blocks[self.length-1] = self.blocks[self.length-2]
             
    def ate_food(self, food):
        distance = ((self.x - food.x)**2  + (self.y - food.y)**2)**0.5
        # if self.x == food.x and self.y == food.y:
        if distance < 12:
            return True
        return False 

    def grow(self):  