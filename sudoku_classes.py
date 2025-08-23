class SudokuGrid:
    def __init__(self):
        self.grid = []
        for row in range(9):
            list = []
            for col in range(9):
                list.append(" ")
            self.grid.append(list)
        self.possibilities = Possibilities()

    def enter_number(self, num, row, col):
        print(f"Entering {num} at coordinates {row}, {col} on the grid.")
        self.grid[row][col] = num
        print(f"Confirming correct entering: {self.grid[row][col]} now equals {num}.")
        print(f"Beginning to remove {num} from possibles in this row and column.")
        for i in range(9):
            print(f"Removing from row {row}, column {i}")
            self.possibilities.remove_possible(num, row, i)
            print(f"Removing from row {i}, column {col}")
            self.possibilities.remove_possible(num, i, col)
        print(f"Possiblities should be removed now. Testing...")
        print(self.possibilities.grid[5][col])
        print(f"The above list shouldn't have the number {num} in it.")

    def print_grid(self):
        for row in self.grid:
            print(row)


class Possibilities(SudokuGrid):
    def __init__(self):
        self.grid = []
        for row in range(9):
            list = []
            for col in range(9):
                list.append(["1", "2", "3", "4", "5", "6", "7", "8", "9"])
            self.grid.append(list)
    
    def remove_possible(self, num, row, col):
        if num in self.grid[row][col]:
            print(f"Found {num} in possibles here, removing it.")
            self.grid[row][col].remove(num)
    
    def is_possible(self, num, row, col):
        return num in self.grid[row][col]