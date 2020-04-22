# Any changes to the distributions library should be reinstalled with
#  pip install --upgrade .

# For running unit tests, use
# /usr/bin/python -m unittest test


class TestPytest:

    def test_initialization(self):
        capacity = 50
        weights = [31, 10, 20, 19, 4, 3, 6]
        profits = [70, 20, 39, 37, 7, 5, 10]
        max_profit = 107
        min_profit = 98
        assert capacity == capacity, "no"
        assert weights == weights, "no"
        assert profits ==  profits, "no"
