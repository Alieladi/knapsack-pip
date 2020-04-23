# knapsack-pip: A 0-1 knapsack solver
This is a library for solving knapsack problems.

Use this solver for maximization or minimization of 0-1 knapsack problems a Branch and Bound algorithm.

Non negative weights and profits can also be included.

## Installation
This library can be installed via pip. Use command: `pip install knapsack-pip`

## Usage
So far, there are different knapsack solvers for different algorithms:
- BBKnapsack: a knapsack solver using branch and bound with a stack. To import: `from knapsack01.BBKnapsack import BBKnapsack`
- HSKnapsack: a knapsack solver using the Horowitz-Sahni branch and bound algorithm. To import: `from knapsack01.HSKnapsack import HSKnapsack`

The output includes the maximum or minimum profit and its corresponding solution as a list of the same length as list of items (solution[i] = 1 if ith item is included in the solution and solution[i] = 0 otherwise)


### Example of maximization
```
from knapsack01.BBKnapsack import BBKnapsack

capacity = 50
weights = [31, 10, 20, 20, 5, 3, -6]
profits = [70, 20, 39, 37, 7, 5, 10]

my_knapsack1 = BBKnapsack(capacity, profits, weights)
max_profit, max_solution = my_knapsack1.maximize()
# (126, [1, 0, 1, 0, 1, 0, 1])
```
### Example of minimization
```
from knapsack01.BBKnapsack import BBKnapsack

capacity = 50
weights = [31, 10, 20, 20, 5, 3, -6]
profits = [70, 20, 39, 37, 7, 5, 10]

my_knapsack2 = BBKnapsack(capacity, profits, weights)
min_profit, min_solution = my_knapsack2.minimize()
# (96, [0, 1, 1, 1, 0, 1, 0])
```
