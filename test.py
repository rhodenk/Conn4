import unittest

import main


class TestMain(unittest.TestCase):

    def _resetGrid(self):
        for r in range(0, main.ROW_COUNT):
            for c in range(0, main.COL_COUNT):
                main.grid[r][c] = "."

    def test_config_vars(self):
        """
        All tests are based on assumption of 6x9 grid.  Confirm the app is still configured like this
        """
        t_ROW_COUNT = main.ROW_COUNT
        t_COL_COUNT = main.COL_COUNT
        t_WIN_COUNT = main.WIN_COUNT
        
        self.assertEqual(t_ROW_COUNT, 6)
        self.assertEqual(t_COL_COUNT, 9)
        self.assertEqual(t_WIN_COUNT, 4)


    # def test_grid_populate(self):
    #     """
    #     Test that all grid cells contain "."
    #     """
    #     for r in range(0, main.ROW_COUNT):
    #         for c in range(0, main.COL_COUNT):
    #             self.assertEqual(main.grid[r][c], ".")

    def test_token_insert(self):
        self._resetGrid()
        main.addToken(0, "R")
        t_colTokens = main.getCol(0)
        self.assertEqual(t_colTokens, "R.....", "Col 0 should only contain one R token")
        for c in range(1, main.COL_COUNT):
            t_colTokens = main.getCol(c)
            self.assertEqual(t_colTokens, "......", f"Col {c} should only contain '.' tokens'")

    def test_column_win(self):
        self._resetGrid()
        for i in range(0,4):
            main.addToken(0, "R")
        t_win = main.checkWin()
        self.assertEqual(t_win, "R", "Should get 'R' win because 4 token in col 0")

    def test_Fdiagonal_win(self):
        self._resetGrid()
        main.addToken(0, "R")
        main.addToken(1, "Y")
        main.addToken(2, "Y")
        main.addToken(3, "Y")
        main.addToken(1, "R")
        main.addToken(2, "Y")
        main.addToken(3, "Y")
        main.addToken(2, "R")
        main.addToken(3, "Y")
        main.addToken(3, "R")

        t_win = main.checkWin()
        self.assertEqual(t_win, "R", "Should get 'R' win because of Fdiagonal tokens")

if __name__ == '__main__':
    unittest.main()