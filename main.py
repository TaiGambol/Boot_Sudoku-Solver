from sudoku_classes import SudokuGrid, Possibilities



def read_sudoku(sudoku_path):
    with open(sudoku_path, "r") as file:
        puzzle = file.read()
    
    puzzle = puzzle.translate({ord(i): None for i in '-+|'})
    rows = puzzle.split("\n")
    rows = [x for x in rows if x]
    grid = SudokuGrid()
    for k, row in enumerate(rows):
        for j, num in enumerate(row):
            if num != ".":
                grid.enter_number(num, k, j)
    return grid

def solve_step(grid):
    pass

def main():
    grid = read_sudoku("./puzzles/puzzle.txt")
    grid.print_grid()
    grid.solve_loop()

main()