import math

class SudokuGrid:
    def __init__(self):
        self.grid = []
        for row in range(9):
            list = []
            for col in range(9):
                list.append(" ")
            self.grid.append(list)
        self.possibilities = Possibilities()
        self.blocks = [(1, 1), (1, 4), (1, 7), (4, 1), (4, 4), (4, 7), (7, 1), (7, 4), (7, 7),]

    def enter_number(self, num, row, col):
        print(f"Entering {num} at coordinates {row}, {col} on the grid.")
        self.grid[row][col] = num
        for i in range(9):
            #print(f"Removing from row {row}, column {i}")
            self.possibilities.remove_possible(num, row, i)
        for i in range(9):
            #print(f"Removing from row {i}, column {col}")
            self.possibilities.remove_possible(num, i, col)
        self.possibilities.remove_possible_in_block(num, row, col)
        
    def print_grid(self):
        for row in self.grid:
            print(row)

    def naked_singles_row(self, num, row):
        #print(f"Checking for naked singles in the area of row {row}")
        num = str(num)
        single = False
        single_row = row
        single_col = 0
        # Checking each cell in the row
        for j in range(9):
            if self.possibilities.grid[row][j] == num and single is not True:
                #print(f"Found a possible match, and no others yet.")
                single = True
                single_col = j
            elif self.possibilities.grid[row][j] == num and single is True:
                #print(f"Found a second possible match, no naked singles here.")
                single = False
                single_col = 0
                break
        if single is True:
            self.enter_number(num, single_row, single_col)


    def naked_singles_col(self, num, col):
        #print(f"Checking for naked singles in the area of column {col}")
        num = str(num)
        single = False
        single_row = 0
        single_col = col
        # Checking each cell in the row
        for j in range(1,9):
            #print(f"Checking cell {j} in column {col}")
            if num in self.possibilities.grid[j][col] and single is not True:
                #print(f"Found a possible match, and no others yet.")
                single = True
                single_row = j
            elif num in self.possibilities.grid[j][col] and single is True:
                #print(f"Found a second possible match, no naked singles here.")
                single = False
                single_row = 0
                break
        if single is True:
            self.enter_number(num, single_row, single_col)

    def naked_singles_block(self, num, row, col):
        #print(f"Checking for naked singles in the area of row {row}, col {col}")
        num = str(num)
        single = False
        single_row = 0
        single_col = 0
        g = row + 1
        h = col + 1
        g2 = math.ceil(g/3)
        h2 = math.ceil(h/3)
        g = g2 * 3
        h = h2 * 3
        g2 = g-3
        h2 = h-3
        for i in range(g2, g):
            for j in range(h2, h):
                #print(f"Checking {i},{j} on the grid")
                if self.possibilities.grid[i][j] == num and single is not True:
                    #print(f"Found a possible match, and no others yet.")
                    single = True
                    single_row = i
                    single_col = j
                elif self.possibilities.grid[i][j] == num and single is True:
                    #print(f"Found a second possible match, no naked singles here.")
                    single = False
                    single_row = 0
                    single_col = 0
                    break
        if single is True:
            self.enter_number(num, single_row, single_col)

    def solve_loop(self):
        print(f"Beginning solution loop.")
        count = 0
        print(f"Initializing counter")
        while count <= 2:
            count += 1
            print(f" We're on pass #{count}")
            for num in range(1,10):
                print(f" Working on solutions for {num}")
                for row in range(9):
                    print(f"  Searching row {row}")
                    self.naked_singles_row(num, row)
                for col in range(9):
                    print(f"  Searching column {col}")
                    self.naked_singles_col(num, col)
                for r,c in self.blocks:
                    print(f"  Searching block at coords {r}, {c}")
                    self.naked_singles_block(num, r, c)
        print(f"Solution loop finished, printing current grid.")
        self.print_grid()

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
    
    def remove_possible_in_block(self, num, row, col):
        #print(f"Running initial math to work out what block we're in.")
        g = row + 1
        h = col + 1
        #print(f"g set to {g}, h set to {h}")
        g2 = math.ceil(g/3)
        h2 = math.ceil(h/3)
        #print(f"{g}/3 ceiling'd = {g2}, {h}/3 ceiling'd = {h2}")
        g = g2 * 3
        h = h2 * 3
        #print(f"{g2}x3 = {g}, {h2}x3 = {h}")
        g2 = g-3
        h2 = h-3
        #print(f"Start points set: row search starting at {g2}, column search starting at {h2}")
        #print(f"Searching for the proper box now.")
        for i in range(g2, g):
            #print(f"We're in row {i}")
            for j in range(h2, h):
                #print(f"We're in column {j}")
                self.remove_possible(num, i, j)
        
    def is_possible(self, num, row, col):
        return num in self.grid[row][col]