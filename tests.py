import unittest
from maze import Maze
from graphics import Window

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        win = Window(120, 100)
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, win)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_create_cells_2(self):
        num_cols = 20
        num_rows = 16
        win = Window(200, 160)
        m1 = Maze(0,0, num_rows, num_cols, 10, 10, win)
        self.assertEqual(
            len(m1._cells),
            num_cols
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows
        )

    def test_maze_break_entrance_and_exit(self):
        num_cols = 12
        num_rows = 10
        win = Window(200,160)
        m1 = Maze(10,10, num_rows, num_cols, 10, 10, win)
        m1._break_entrance_and_exit()
        self.assertEqual(
            m1._cells[0][0].has_top_wall, False,
        )
        self.assertEqual(
            m1._cells[num_cols - 1][num_rows - 1].has_bottom_wall, False
        )

    def test_maze_reset_cells_visted(self):
        num_cols = 12
        num_rows = 10
        win = Window(200,160)
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, win)
        for col in m1._cells:
            for cell in col:
                self.assertEqual(
                    cell.visited,
                    False,
                )

if __name__ == "__main__":
    unittest.main()