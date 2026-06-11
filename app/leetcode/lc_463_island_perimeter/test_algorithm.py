import importlib
import unittest

# Using importlib because of numeric characters in package name
algorithm = importlib.import_module("app.leetcode.lc_463_island_perimeter.algorithm")
Solution = algorithm.Solution

class TestIslandPerimeter(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        # Example 1: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]], Output: 16
        grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
        self.assertEqual(self.solution.islandPerimeter(grid), 16)

    def test_example2(self):
        # Example 2: grid = [[1]], Output: 4
        grid = [[1]]
        self.assertEqual(self.solution.islandPerimeter(grid), 4)

    def test_example3(self):
        # Example 3: grid = [[1,0]], Output: 4
        grid = [[1,0]]
        self.assertEqual(self.solution.islandPerimeter(grid), 4)

    def test_single_row(self):
        # grid = [[1,1,1]], Output: 8
        grid = [[1,1,1]]
        self.assertEqual(self.solution.islandPerimeter(grid), 8)

    def test_single_column(self):
        # grid = [[1],[1],[1]], Output: 8
        grid = [[1],[1],[1]]
        self.assertEqual(self.solution.islandPerimeter(grid), 8)

    def test_disconnected_island_not_possible_by_desc_but_logic_should_work(self):
        # Desc says exactly one island, but let's check basic logic
        grid = [[1,0,1]]
        self.assertEqual(self.solution.islandPerimeter(grid), 8)

if __name__ == "__main__":
    unittest.main()
