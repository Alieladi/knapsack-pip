class Knapsack:

	def __init__(self, capacity=0, profits=[], weights=[]):
		""" Knapsack class for solving a knapsack problem.

		Attributes:
			profits (list of non-negative floats): profits of items
			weights (list of positive floats): weights of items
			nb_items (int): number of items
			ids: (list of ints): ids of items
			capacity (float): capacity of knapsack
		"""
		self.profits = profits
		self.weights = weights
		self.nb_items = len(profits)
		self.capacity = capacity


	def read_data_file(self, file_name):
		"""Function to read in data from a txt file. The txt file should have
		two floats per line separated by comma representing the profit and the
        weight respectively.

		Args:
			file_name (string): name of a file to read from

		Returns:
			None
		"""
		with open(file_name) as file:
			line = file.readline()
			while line:
				profit, weight = line.split(',')
				self.profits.append(profit)
				self.weights.append(weight)
				self.nb_items = len(profits)
				self.capacity = capacity
				line = file.readline()
		file.close()


	def sort_by_ratio(self):
		"""Function to sort item indexes by their ratios profit/weight in a
		descending order.

		Args:
			None

		Returns:
			sorted (list of ints): item_ids sorted by profit/weight in a
									descending order
		"""
		self.ids = sorted(self.ids, key=lambda i: self.profits[i]/self.weights[i],
						reverse=True)

	def maximize(self, positive_only):
		"""Function to compute the solution to the knapsack problem.
		Some easy cases are treated in this class as the code is same in all
		subclasses. The rest must be defined in subclasses

		Args:
			None
		Returns:
			max_solution (list of ints): ids of the best set of items
			max_profit (float): best profit
		"""
		self.max_profit = 0
		self.max_solution = [0]*self.nb_items
		self.ids = list(range(self.nb_items))

		"""# easy case condition (optional):
		# the sum of weights is less or equal to capacity
		done = False
		cumul_weights = 0
		i = 0
		while cumul_weights < self.capacity:
			cumul_weights += self.profits[i]
			i += 1
		if i == self.length:
			self.max_profit = sum(self.profits)
			self.max_solution = [1]*self.len
			done = True
			return done"""

		self.Nzero_ids = []
		self.None_ids = []
		self.Nminus_ids = []
		self.Nplus_ids = self.ids

		if not positive_only:
			# 2nd condition: Non positive values in weight and profit
			self.Nzero_ids = []
			self.None_ids = []
			self.Nminus_ids = []
			self.Nplus_ids = []
			for i in self.ids:
				# Group N0
				if self.weights[i] >= 0 and self.profits[i] <= 0:
					self.max_solution[i] = 0
					self.Nzero_ids.append(i)
				# Group N1
				elif self.weights[i] <= 0 and self.profits[i] >= 0:
					self.max_solution[i] = 1
					self.max_profit += self.profits[i]
					self.capacity -= self.weights[i]
					self.None_ids.append(i)
				# Group N-
				elif self.weights[i] < 0 and self.profits[i] < 0:
					self.max_profit += self.profits[i]
					self.capacity -= self.weights[i]
					# then change sign
					self.weights[i] *= -1
					self.profits[i] *= -1

					self.Nminus_ids.append(i)
				# Group N+
				else:
					self.Nplus_ids.append(i)

			self.ids = self.Nminus_ids + self.Nplus_ids
			self.len = len(self.ids)# self.len = len(self.ids) all time



	def minimize(self):
		"""Function to compute the solution to the minimization version of
		knapsack problem. The problem is to minimize the "profits" given a
		minimum capacity that the sum of weights need to be at least equal to.
		"""
		self.capacity = sum(self.weights) - self.capacity
		self.min_profit = sum(self.profits)
		self.maximize()
		self.min_solution = [1-x for x in self.max_solution]
		self.min_profit -= self.max_profit
		return self.min_profit, self.min_solution
