import importlib
import unittest


algorithm = importlib.import_module(
    "app.leetcode.lc_806_number_of_lines_to_write_string.algorithm"
)
Solution = algorithm.Solution


class TestNumberOfLinesToWriteString(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        widths = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10,
                  10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
        self.assertEqual(
            self.solution.numberOfLines(widths, "abcdefghijklmnopqrstuvwxyz"),
            [3, 60],
        )

    def test_example2(self):
        widths = [4, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10,
                  10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
        self.assertEqual(
            self.solution.numberOfLines(widths, "bbbcccdddaaa"),
            [2, 4],
        )

    def test_single_line(self):
        widths = [2] * 26
        self.assertEqual(self.solution.numberOfLines(widths, "leetcode"), [1, 16])

    def test_exactly_full_line(self):
        widths = [10] * 26
        self.assertEqual(self.solution.numberOfLines(widths, "abcdefghij"), [1, 100])

    def test_new_line_after_full_line(self):
        widths = [10] * 26
        self.assertEqual(self.solution.numberOfLines(widths, "abcdefghijk"), [2, 10])


if __name__ == "__main__":
    unittest.main()
