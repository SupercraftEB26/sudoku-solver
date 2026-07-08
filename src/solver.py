from src.board import Board

def solve(board):
    if board.is_full():
        return True
    
    x, y = board.next_empty()

    for move in range(1, 10):
        if board.is_valid_move(x, y, move):
            board.set(x, y, move)

            if solve(board):
                return True
            
            board.set(x, y, 0)
    return False