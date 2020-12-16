import random, os

class Board:

    def __init__(self):
        self.height = os.get_terminal_size().lines # Sets the height of board based on terminal size
        self.width = os.get_terminal_size().columns # Sets the width of board based on terminal size
        self.cells = [[ False for x in range(self.width) ] for y in range(self.height) ]

    def generate(self, rand_max=5):
        '''
            Generates all slots for the board
        '''
        
        for x in range(0, self.width):
            for y in range(0, self.height):
                self.cells[y][x] = self.getRandomState(rand_max)

    def getRandomState(self, rand_max):
        return random.randint(0, rand_max) == 0

    def getCells(self):
        return self.cells