from GeneralKnapsack import Knapsack
import time

class HMKnapsack(Knapsack):

	def __init__(self, capacity=0, profits=[], weights=[]):

		""" Knapsack class for solving a knapsack problem
            by the Horowitz-Sahni branch and bound algorithm

		Attributes:
			profits (list of non-negative floats): profits of items
			weights (list of positive floats): weights of items
			len (int): number of items
			ids: (list of ints): ids of items
			capacity (float): capacity of knapsack
		"""

		Knapsack.__init__(self, capacity, profits, weights)


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
		if i == -1:
			return "END"
		else:
			return "REPEAT"


	def forward_step(self): # keep going to the left
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
					while self.max_profit >= self.curr_profit + self.upper_bound():
						state = self.backtrack()
						if state == "END":
							return

			# update solution:
			if self.curr_profit > self.max_profit:
				self.max_profit = self.curr_profit
				self.max_node = self.curr_node.copy()
				print("update")
				print(self.max_profit)
				print(self.max_node)


			self.level = n - 1
			item_id = self.ids[self.level]
			if self.curr_node[item_id] == 1:
				self.curr_node[item_id] = 0
				self.remaining_capacity += item_weight
				self.curr_profit -= self.profits[item_id]
			state = self.backtrack()
			if state == "END":
				return
			while self.max_profit >= self.curr_profit + self.upper_bound():
				state = self.backtrack()
				if state == "END":
					return


	def maximize(self):
		""" Function to solve the knapsack problem

		Args:
			None
		Returns:
			max_node (list of ints): ids of the best set of items
			max_profit (float): best profit
		"""

		# Some conditions first
		# Check if sum_weights <= self.capacity:
		cumul_weights = 0
		i = 0
		while cumul_weights < self.capacity:
			cumul_weights += self.profits[i]
			i += 1
		if i == self.len:
			self.max_profit = sum(self.profits)
			self.max_node = [1]*self.len
		# Otherwise:
		else:
			self.max_node = []
			self.max_profit = 0

			self.curr_node = [0]*self.len
			self.curr_profit = 0
			self.remaining_capacity = self.capacity
			self.level = 0

			# sort ids by their ratios
			self.sort_by_ratio()

			# solve
			self.forward_step()
		#return self.max_profit, self.max_node



if __name__ == "__main__":
	capacity = 50
	weights = [31, 10, 20, 20, 4, 3, 6]
	profits = [70, 20, 39, 37, 7, 5, 10]
	start = time.time()
	saki = BBKnapsack(capacity, profits, weights)
	saki.maximize()
	print('Duration: {} seconds'.format(time.time() - start))

	print("final result")
	print(saki.max_profit)
	print(saki.max_node)
