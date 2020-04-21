class Knapsack:

	def __init__(self, capacity=0, profits=[], weights=[]):
		""" Knapsack class for solving a knapsack problem.

		Attributes:
			profits (list of non-negative floats): profits of items
			weights (list of positive floats): weights of items
			len (int): number of items
			ids: (list of ints): ids of items
			capacity (float): capacity of knapsack
		"""
		self.profits = profits
		self.weights = weights
		self.len = len(profits)
		self.ids = list(range(self.len))
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
				self.len = len(profits)
				self.ids = list(range(self.length))
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

	def convert_max():
		""" convert a minimization problem to a maximization problem
		"""
		pass
