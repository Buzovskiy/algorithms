import unittest
from .algorithm import Solution

class TestAlgorithm(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        self.assertEqual(self.solution.findLHS([1,3,2,2,5,2,3,7]), 5)

    def test_example2(self):
        self.assertEqual(self.solution.findLHS([1,2,3,4]), 2)

    def test_example3(self):
        self.assertEqual(self.solution.findLHS([1,1,1,1]), 0)

if __name__ == '__main__':
    unittest.main()
