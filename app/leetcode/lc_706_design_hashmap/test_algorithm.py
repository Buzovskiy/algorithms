import importlib
import unittest


algorithm = importlib.import_module("app.leetcode.lc_706_design_hashmap.algorithm")
MyHashMap = algorithm.MyHashMap


class TestDesignHashMap(unittest.TestCase):
    def test_example1(self):
        my_hash_map = MyHashMap()
        self.assertIsNone(my_hash_map.put(1, 1))
        self.assertIsNone(my_hash_map.put(2, 2))
        self.assertEqual(my_hash_map.get(1), 1)
        self.assertEqual(my_hash_map.get(3), -1)
        self.assertIsNone(my_hash_map.put(2, 1))
        self.assertEqual(my_hash_map.get(2), 1)
        self.assertIsNone(my_hash_map.remove(2))
        self.assertEqual(my_hash_map.get(2), -1)


if __name__ == "__main__":
    unittest.main()
