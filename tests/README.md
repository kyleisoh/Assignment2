## Running a single test module
To run a single test module, in this case, test_checkoutcalculator.py
```
$ python -m unittest test.test_antigravity
```

## To run a single TestCase or a single test method:
```
$ python -m unittest test.test_antigravity.GravityTestCase
$ python -m unittest test.test_antigravity.GravityTestCase.test_method
```

## To run all tests
[Test discovery](https://docs.python.org/2/library/unittest.html#test-discovery) which will discover and run all the tests for you, they must be modules or packages named test*.py (can be changed with the -p, --pattern flag):

```
$ python -m unittest discover
```