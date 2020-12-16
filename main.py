from src.board import Board
from src.game import Game

def main():
    # Create board object to initialise the first state, based on random data
    board = Board()
    board.generate()

    # Starts game with configured board
    game = Game(board.getCells())
    game.nextGen()

if __name__ == '__main__':
    main()