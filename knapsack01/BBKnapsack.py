from .Knapsack import Knapsack
import time

class BBKnapsack(Knapsack):

	def __init__(self, capacity=0, profits=[], weights=[]):

		""" Knapsack class for solving a knapsack problem
            by branch and bound. The process can be represented
			as searching a binary tree.
			Each level represents an item, and each node represents an item set.
			The decision at each node is whether to include the item of the
			level index, which results in 2 children nodes.

		Attributes:
			profits (list of non-negative floats): profits of items
			weights (list of positive floats): weights of items
			len (int): number of items
			ids: (list of ints): ids of items
			capacity (float): capacity of knapsack
		"""

		Knapsack.__init__(self, capacity, profits, weights)


	def upper_bound(self, level, remaining_capacity):
		""" Function to compute the upper bound at level

		Args:
			level (int): level of the tree.
			remaining_capacity (float) remaining capacity
		Returns:
			upper_bound (float): upper bound
		"""

		temp_capacity = remaining_capacity
		upper_bound = 0
		n = self.len
		j = level
		j_id = self.ids[j]
		j_weight = self.weights[j_id]

		## optimization (test)
		while (temp_capacity < j_weight) and (j < n-1):
			j += 1
			j_id = self.ids[j]
			j_weight = self.weights[j_id]
		### end optimization

		while temp_capacity >= j_weight:
			# update upper_bound and capacity
			upper_bound += self.profits[j_id]
			temp_capacity -= j_weight

			# next potential addition
			j += 1
			if j == n:
				break
			j_id = self.ids[j]
			j_weight = self.weights[j_id]

		if j < n:
			upper_bound += temp_capacity * (self.profits[j_id]/j_weight)

		return upper_bound

	def maximize(self, positive_only=False):
		""" Function to solve the knapsack problem

		Args:
			None
		Returns:
			max_solution (list of ints): ids of the best set of items
			max_profit (float): best profit
		"""
		super().maximize(positive_only)

		max_node = []
		max_profit = 0

		# solve problem
		node = []
		profit = 0
		level = 0
		capacity = self.capacity

		stack = [(level, node, capacity, profit)]
		while stack:
			level, node, capacity, profit = stack.pop()
			if level == self.len-1:
				item_id = self.ids[level]
				item_weight = self.weights[item_id]
				capacity = capacity - item_weight
				if capacity >= 0:
					item_profit = self.profits[item_id]
					profit += item_profit
				if profit > max_profit:
					max_node = node
					max_profit = profit
					"""print("update -----")
					print("profit", max_profit)
					print("node", max_solution)
					print("------------")"""

				continue

			# Include right child ?
			right_level = level + 1
			upper_bound = self.upper_bound(right_level, capacity)
			if (max_profit < profit + upper_bound):
				right_child = (right_level, node, capacity, profit)
				stack.append(right_child)

			# Include left child ?
			item_id = self.ids[level]
			item_weight = self.weights[item_id]
			item_profit = self.profits[item_id]
			left_capacity = capacity - item_weight
			if left_capacity >= 0:
				left_profit = profit + item_profit
				upper_bound = self.upper_bound(level, capacity)
				if (max_profit < left_profit + upper_bound):
					left_solution = node + [item_id]
					left_level = level + 1
					left_child = (left_level, left_solution, left_capacity, left_profit)
					stack.append(left_child)

		# fill solution
		self.max_profit += max_profit

		for i in max_node:
			 self.max_solution[i] = 1
		for i in self.Nminus_ids:
			self.max_solution[i] = 1-self.max_solution[i]

		return self.max_profit, self.max_solution





if __name__ == "__main__":
	capacity = 50
	weights = [31, 10, 20, 20, 4, 3, -6]
	profits = [70, 20, 39, 37, 7, 5, 10]
	start = time.time()
	saki = BBKnapsack(capacity, profits, weights)
	saki.maximize()
	print('Duration: {} seconds'.format(time.time() - start))

	print("final result")
	print(saki.max_profit)
	print(saki.max_solution)

	saki = BBKnapsack(capacity, profits, weights)
	saki.minimize()
	print("final min result")
	print(saki.min_profit)
	print(saki.min_solution)
