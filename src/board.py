class Board:
    def __init__(self, grid):
        self.grid = grid

    @classmethod
    def from_file(self, path):
        grid = []

        with open(path, "r") as file:
            for line in file:
                line = line.strip()
                row = [int(char) for char in line]
                grid.append(row)
        
        return Board(grid)

    def __str__(self):
        output = ""

        for row in self.grid:
            output += " ".join(str(value) for value in row)
            output += "\n"
        
        return output

    def get(self, x, y):
        return self.grid[y][x]
    
    def set(self, x, y, value):
        self.grid[y][x] = value

    def is_empty(self, x, y):
        return self.grid[y][x] == 0

    def column(self, x):
        output = []

        for y in range(9):
            output.append(self.grid[y][x])

        return output

    def square(self, x, y):
        output = []

        square_x = x // 3
        square_y = y // 3

        for check_y in range(9):
            for check_x in range(9):
                if (square_x == check_x // 3
                and square_y == check_y // 3):
                    output.append(self.grid[check_y][check_x])
        
        return output

    def is_valid_move(self, x, y, value):
        if value in self.grid[y]:
            return False
        if value in self.column(x):
            return False
        if value in self.square(x, y):
            return False
        return True

    def is_full(self):
        for y in range(9):
            if 0 in self.grid[y]:
                return False
        return True
    
    def next_empty(self):
        for y in range(9):
            for x in range(9):
                if self.grid[y][x] == 0:
                    return(x, y)
        return (0, 0)