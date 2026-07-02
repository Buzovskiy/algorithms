import importlib
import unittest


algorithm = importlib.import_module("app.leetcode.lc_705_design_hashset.algorithm")
MyHashSet = algorithm.MyHashSet


class TestDesignHashSet(unittest.TestCase):
    def test_example1(self):
        my_hash_set = MyHashSet()
        self.assertIsNone(my_hash_set.add(1))
        self.assertIsNone(my_hash_set.add(2))
        self.assertTrue(my_hash_set.contains(1))
        self.assertFalse(my_hash_set.contains(3))
        self.assertIsNone(my_hash_set.add(2))
        self.assertTrue(my_hash_set.contains(2))
        self.assertIsNone(my_hash_set.remove(2))
        self.assertFalse(my_hash_set.contains(2))


if __name__ == "__main__":
    unittest.main()
