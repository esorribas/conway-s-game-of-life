import time, os

class Game:

    def __init__(self, board):
        self.board = board
        self.height = os.get_terminal_size().lines # Sets the height of board based on terminal size
        self.width = os.get_terminal_size().columns # Sets the wiodth of board based on terminal size

    def nextGen(self):
        '''
            Detects if exist alive cells to print, if exist at least one alive cell continues the game,
            if not, the game is over and stop iterating
        '''

        exists_alive_cells = any(any(row) for row in self.board)

        while exists_alive_cells:
            dead_items = []
            alive_items = []

            time.sleep(1)
            self.render()

            for y in range(self.height):
                for x in range(self.width):
                    alive_neighbour_count = self.getAliveNeighbourCount(x, y)

                    # If cell is alive and has more than 3 or less than 2 neighbors, this cell becomes to dead status
                    if self.board[y][x] and (alive_neighbour_count < 2 or alive_neighbour_count > 3):
                        dead_items.append([y, x])

                    # If cell is dead and has 3 neighbours, this cell becomes to live status
                    if not self.board[y][x] and alive_neighbour_count == 3:
                        alive_items.append([y, x])

            # Iterates over detected dead item list and set related cells to False (Dead)
            for dead_item in dead_items:
                self.board[dead_item[0]][dead_item[1]] = False
            
            # Iterates over detected alive item list and set related cells to True (Alive)
            for alive_item in alive_items:
                self.board[alive_item[0]][alive_item[1]] = True

            # Checks if still exists alive cells
            exists_alive_cells = any(any(row) for row in self.board)

        print('Game is over :(')

    def getAliveNeighbourCount(self, x, y):
        '''
            Checks how many alive neighbours has a cell by index
        '''

        count = 0
        prev_x = (x - 1)
        next_x = (x + 1)
        prev_y = (y - 1)
        next_y = (y + 1)

        for check_y in range(prev_y, next_y):
            # Out of range, continue
            if check_y < 0 or check_y >= self.height:
                continue
            
            for check_x in range(prev_x, next_x):
                # Current cell, continue
                if check_x == x and check_y == y:
                    continue
                
                # Out of range, continue
                if check_x < 0 or check_x >= self.width:
                    continue
                
                if self.board[check_y][check_x]:
                    count += 1
        return count

    def render(self):
        '''
            Iterates on every row and cell and determines which cells are alive or not
            and representing them by a O or - symbol (O means alive cell, - means dead cell)
        '''
        for row in self.board:
            render_string = ''

            for cell in row:
                render_string += 'O' if cell else '-'

            print(render_string)