from solvers.BBKnapsack import BBKnapsack
from solvers.HSKnapsack import HSKnapsack

capacity = 50
weights = [31, 10, 20, 19, 4, 3, 6]
profits = [70, 20, 39, 37, 7, 5, 10]
max_profit = 107
min_profit = 98

class TestHSKnapsackClass():

    def test_maximize(self):
        knapsack = HSKnapsack(capacity, profits, weights)
        cal_profit, cal_solution = knapsack.maximize()
        assert cal_profit == max_profit, 'calculated maximum profit not as expected'
        profit = 0
        for i in range(knapsack.nb_items):
            if cal_solution[i] == 1:
                profit += knapsack.profits[i]
        assert profit == max_profit, 'calculated max profit from solution not as expected'

    def test_minimize(self):
        knapsack = HSKnapsack(capacity, profits, weights)
        cal_profit, cal_solution = knapsack.minimize()
        assert cal_profit == min_profit, 'calculated maximum profit not as expected'
        profit = 0
        for i in range(knapsack.nb_items):
            if cal_solution[i] == 1:
                profit += knapsack.profits[i]
        assert profit == min_profit, 'calculated min profit from solution not as expected'



class TestBBKnapsackClass():

    def test_maximize(self):
        knapsack = BBKnapsack(capacity, profits, weights)
        cal_profit, cal_solution = knapsack.maximize()
        assert cal_profit == max_profit, 'calculated maximum profit not as expected'
        profit = 0
        for i in range(knapsack.nb_items):
            if cal_solution[i] == 1:
                profit += knapsack.profits[i]
        assert profit == max_profit, 'calculated max profit from solution not as expected'

    def test_minimize(self):
        knapsack = BBKnapsack(capacity, profits, weights)
        cal_profit, cal_solution = knapsack.minimize()
        assert cal_profit == min_profit, 'calculated maximum profit not as expected'
        profit = 0
        for i in range(knapsack.nb_items):
            if cal_solution[i] == 1:
                profit += knapsack.profits[i]
        assert profit == min_profit, 'calculated min profit from solution not as expected'
