from .Knapsack import Knapsack
import time

class HSKnapsack(Knapsack):

	def __init__(self, capacity=0, profits=[], weights=[]):

		""" Knapsack class for solving a knapsack problem
            by the Horowitz-Sahni branch and bound algorithm

		Attributes:
			profits (list of non-negative floats): profits of items
			weights (list of positive floats): weights of items
			length (int): number of items
			ids: (list of ints): ids of items
			capacity (float): capacity of knapsack
		"""

		super().__init__(capacity, profits, weights)


	def upper_bound(self):
		""" Function to compute the upper bound at level

		Args:
			None
		Returns:
			upper_bound (float): upper bound
		"""

		temp_capacity = self.remaining_capacity
		upper_bound = 0
		n = self.len
		j = self.level
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


	def backtrack(self):
		i = self.level - 1
		while i >= 0:
			item_id = self.ids[i]
			if self.curr_node[item_id] == 1:
				self.curr_node[item_id] = 0
				self.remaining_capacity += self.weights[item_id]
				self.curr_profit -= self.profits[item_id]
				self.level = i + 1
				break
			i -= 1

		repeat = True
		if i == -1:
			repeat = False
		return repeat


	def hs_algo(self): # keep going to the left

		self.level = 0
		self.curr_node = self.max_solution.copy()
		self.curr_profit = 0
		self.remaining_capacity = self.capacity

		max_profit = 0
		max_node = self.curr_node

		n = self.len
		while True:
			while self.level < n:
				item_id = self.ids[self.level]
				item_weight = self.weights[item_id]

				while (self.remaining_capacity >= item_weight):
					self.curr_profit += self.profits[item_id]
					self.remaining_capacity -= item_weight
					self.curr_node[item_id] = 1
					self.level += 1
					if self.level < n:
						item_id = self.ids[self.level]
						item_weight = self.weights[item_id]
					else:
						break

				if self.level < n:
					item_id = self.ids[self.level]
					self.curr_node[item_id] = 0
					self.level += 1

				# compute upper bound
				if self.level < n-1:
					while max_profit >= self.curr_profit + self.upper_bound():
						repeat = self.backtrack()
						if repeat == False:
							return max_profit, max_node

			# update solution:
			if self.curr_profit > max_profit:
				max_profit = self.curr_profit
				max_node = self.curr_node.copy()
				"""
				print("update")
				print(max_profit)
				print(max_node)
				"""
			self.level = n - 1
			item_id = self.ids[self.level]
			if self.curr_node[item_id] == 1:
				self.curr_node[item_id] = 0
				self.remaining_capacity += item_weight
				self.curr_profit -= self.profits[item_id]

			# backtrack
			repeat = self.backtrack()
			if repeat == False:
				return max_profit, max_node
			while max_profit >= self.curr_profit + self.upper_bound():
				repeat = self.backtrack()
				if repeat == False:
					return max_profit, max_node


	def maximize(self, positive_only=False):
		""" Function to solve the knapsack problem

		Args:
			None
		Returns:
			max_solution (list of ints): ids of the best set of items
			max_profit (float): best profit
		"""
		# super extra steps
		super().maximize(positive_only)
		# sort ids by their ratios
		self.sort_by_ratio()
		# solve
		max_profit, max_node = self.hs_algo()

		self.max_profit += max_profit
		for i in self.Nplus_ids:
			self.max_solution[i] = max_node[i]
		for i in self.Nminus_ids:
			self.max_solution[i] = 1-max_node[i]

		return self.max_profit, self.max_solution



if __name__ == "__main__":
	capacity = 50
	weights = [31, 10, 20, 20, 5, 3, -6]
	profits = [70, 20, 39, 37, 7, 5, 10]
	start = time.time()
	saki = HSKnapsack(capacity, profits, weights)
	saki.maximize()
	print('Duration: {} seconds'.format(time.time() - start))

	print("final max result")
	print(saki.max_profit)
	print(saki.max_solution)

	saki = HSKnapsack(capacity, profits, weights)
	saki.minimize()
	print("final min result")
	print(saki.min_profit)
	print(saki.min_solution)
