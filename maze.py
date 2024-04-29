from cell import Cell
import random
import time

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win, seed = None, ):
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        if seed:
            random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0,0)
        self._reset_cells_visited()

    def _create_cells(self):
        for x in range(0,self._num_cols):
            col_cells = []
            for y in range(0,self._num_rows):
                col_cells.append(Cell(self._win ))
            self._cells.append(col_cells)
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i,j)

    def _draw_cell(self, i, j):
        if self._win is None:
            return
        x1 = self._x1 + i * self._cell_size_x
        y1 = self._y1 + j * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0,0)
        self._cells[self._num_cols - 1][self._num_rows -1].has_bottom_wall = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            adjacent_cells = []
            if (i-1 >= 0) and (not self._cells[i-1][j].visited):
                adjacent_cells.append((i-1, j))
            if (i+1 < len(self._cells)) and (not self._cells[i+1][j].visited):
                adjacent_cells.append((i+1, j))
            if (j-1 >= 0) and (not self._cells[i][j-1].visited):
                adjacent_cells.append((i, j-1))
            if (j+1 < len(self._cells[i])) and (not self._cells[i][j+1].visited):
                adjacent_cells.append((i, j+1))
            if adjacent_cells == []:
                self._draw_cell(i,j)
                return
            chosen_i, chosen_j = random.choice(adjacent_cells)
            if chosen_j < j:
                self._cells[i][j].has_top_wall = False
                self._cells[chosen_i][chosen_j].has_bottom_wall = False
            elif chosen_j > j:
                self._cells[i][j].has_bottom_wall = False
                self._cells[chosen_i][chosen_j].has_top_wall = False
            elif chosen_i < i:
                self._cells[i][j].has_left_wall = False
                self._cells[chosen_i][chosen_j].has_right_wall = False
            elif chosen_i > i:
                self._cells[i][j].has_right_wall = False
                self._cells[chosen_i][chosen_j].has_left_wall = False

            self._break_walls_r(chosen_i, chosen_j)         

    def _reset_cells_visited(self):
        for col in self._cells:
            for cell in col:
                cell.visited = False
        
    #returns True if this is the end cell, OR if it leads to the end cell.
    #returns False if this is a loser cell.    
    def _solve_r(self, i, j):
        self._animate()
        
        #visit the current cell
        self._cells[i][j].visited = True
        
        #if we are at the end cell, we are done!
        if i == self._num_cols-1 and j == self._num_rows-1:
            return True
        
        #move left if there is no wall and it hasn't been visited
        if (
            i > 0
            and not self._cells[i][j].has_left_wall
            and not self._cells[i-1][j].visited
        ):
            self._cells[i][j].draw_move(self._cells[i-1][j])
            if self._solve_r(i-1, j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i-1][j], True)
        
        #move right if there is no wall and it hasn't been visited
        if(
            i < self._num_cols-1
            and not self._cells[i][j].has_right_wall
            and not self._cells[i+1][j].visited
        ):
            self._cells[i][j].draw_move(self._cells[i+1][j])
            if self._solve_r(i+1,j):
                True
            else:
                self._cells[i][j].draw_move(self._cells[i+1][j], True)

        # move up if there is no wall and it hasn't been visited
        if (
            j > 0
            and not self._cells[i][j].has_top_wall
            and not self._cells[i][j - 1].visited
        ):
            self._cells[i][j].draw_move(self._cells[i][j - 1])
            if self._solve_r(i, j - 1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j - 1], True)

        # move down if there is no wall and it hasn't been visited
        if (
            j < self._num_rows - 1
            and not self._cells[i][j].has_bottom_wall
            and not self._cells[i][j + 1].visited
        ):
            self._cells[i][j].draw_move(self._cells[i][j + 1])
            if self._solve_r(i, j + 1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j + 1], True)

        # we went the wrong way let the previous cell know by returning False
        return False
    
    def solve(self):
        return self._solve_r(0,0)