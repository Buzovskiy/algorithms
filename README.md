# My Algorithms
Algorithms are located in the `app` folder, organized into individual packages.

### Running Tests
To run all tests from the project root:
```

```

To run tests for a specific algorithm:
```
py -3 -m unittest app/leetcode/two_sum/test_algorithm.py
```

To run a single test case:
```
py -3 -m unittest app.leetcode.two_sum.test_algorithm.TwoSumTestCase.test_two_sum
```


py -3 -m unittest discover -p "test_algorithm.py"