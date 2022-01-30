import unittest
from src.fibonacci import fib


class TestFibonacci(unittest.TestCase):
    def test_fib(self):
        self.assertEqual(fib(1), 1, 'should be 1')
        self.assertEqual(fib(2), 1, 'should be 1')
        self.assertEqual(fib(7), 13, 'should be 13')


if __name__ == '__main__':
    unittest.main()
