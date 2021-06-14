import math

#Gameboard class
class Gameboard:

    #if as_string = false then another gameboard object is expected
    #order only relevant for FIFO in priority queue
    def __init__(self, state, as_string = True, path = "", order = 0):
        if as_string:
            #optional way to keep track of path, makes analyzing output easier
            self.path = path
            self.order = order

            #not necessary but make for easier coding
            self.rows = int(math.sqrt(len(state)))
            self.columns = self.rows

            self.flat = []
            self.grid = []
            for c in range(self.columns):
                self.grid.append([0]*self.rows)
            r = 0
            c = 0
            #Convert string to 2D array
            for ch in state:
                self.flat.append(ch)
                self.grid[r][c] = ch
                #store location of empty block
                if(ch == " "):
                    self.blank = (r,c)
                c += 1
                if c >= self.columns:
                    r += 1
                    c = 0
        else:
            self.path = path
            self.order = order
            self.rows = state.rows
            self.columns = state.columns
            self.grid = state.grid.copy()
            self.blank = state.blank

    # r = right, d = down, l = left, u = up
    def can_move(self,direction = 'r'):
        if direction == 'r':
            return self.blank[1] < self.rows - 1
        elif direction == 'd':
            return self.blank[0] < self.columns - 1
        elif direction == 'l':
            return self.blank[1] > 0
        else:
            return self.blank[0] > 0

    #Check for solvability
    def is_solvable(self):
        N = len(self.flat)
        parity1 = 0
        parity2 = 0
        row = 0
        for i in range(N):
            if i % self.rows == 0:
                row += 1
            if self.flat[i] == " ":
                continue
            for j in range(i+1,N):
                if((self.flat[i] > self.flat[j])and self.flat[j] != " "):
                    parity1 +=1
                    #For EF and FE ending variation
                if ((self.flat[i] > self.flat[j] or(self.flat[i] == "E" and self.flat[j] == "F"))\
                        and(self.flat[i] != "F" and self.flat[j] != "E")and self.flat[j] != " "):
                    parity2 += 1

        if self.rows % 2 == 0:
            if self.blank[0] % 2 == 1:
                return parity1 % 2 == 0 or parity2 % 2 == 0
            else:
                return parity1 %2 != 0 or parity2 %2 != 0
        else:
            return parity1 % 2 == 0 or parity2 % 2 == 0


    # r = right, d = down, l = left, u = up
    # move the empty spot in the corresponding direction
    def move(self,direction = 'r'):
        row = self.blank[0]
        col = self.blank[1]
        newRow = row
        newCol = col
        if self.can_move(direction):
            if direction == 'r':
                newCol = col+1
            elif direction == 'd':
                newRow = row+1
            elif direction == 'l':
                newCol = col-1
            else:
                newRow = row-1

        self.grid[row][col] = self.grid[newRow][newCol]
        self.grid[newRow][newCol] = " "
        self.blank = (newRow,newCol)
        self.path += direction

    #less than
    def __lt__(self, other):
        return self.order < other.order
    #equals
    def __eq__(self, other):
        return self.grid == other.grid
    #copy definition
    def __copy__(self):
        return Gameboard(self, as_string = False)
    #string representation
    def __str__(self):
        output = ""
        for row in range(self.rows):
            output += str(self.grid[row]) + '\n'
        return output
