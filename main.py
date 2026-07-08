from argparse import ArgumentParser
from src.board import Board
from src.solver import solve

def main():
    parser = ArgumentParser(description="Sudoku Solver")

    parser.add_argument(
        "file",
        help="Path to the sudoku puzzle"
    )

    args = parser.parse_args()

    board = Board.from_file(args.file)

    print("Original board: ")
    print(str(board))

    solve(board)

    print("Solved board: ")
    print(str(board))

if __name__ == "__main__":
    main()