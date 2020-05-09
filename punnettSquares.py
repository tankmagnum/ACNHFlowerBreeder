from collections import OrderedDict


class PunnettSquare:
	def __init__(self, flower1, flower2, gene_list):
		self.flower1 = flower1
		self.flower2 = flower2
		self.gene_list = gene_list
		self.full_data = []

	# noinspection PyTypeChecker
	def generateTable(self):
		gene1 = self.gene_list.get(self.flower1)
		gene2 = self.gene_list.get(self.flower2)
		column_headers = []
		row_headers = []

		for i in range(2):
			for j in range(2):
				for k in range(2):
					column_headers.append(gene1[0 + i] + gene1[2 + j] + gene1[4 + k])
					row_headers.append(gene2[0 + i] + gene2[2 + j] + gene2[4 + k])
		# print(column_headers)
		# print(row_headers)

		grid_size = len(column_headers)
		data = [[None] * grid_size for x in range(grid_size)]

		for y in range(grid_size):

			for x in range(grid_size):
				x: int
				# Create the grid
				# Specifically go in order of Capital then lower case
				# Specifically go in order RYW
				cell_list = sorted(list(column_headers[x][0] + row_headers[y][0])) + sorted(
					list(column_headers[x][1] + row_headers[y][1])) + sorted(
					list(column_headers[x][2] + row_headers[y][2]))
				# cell is now an list of chars, turn it back into a string
				cell = ''.join(cell_list)
				data[y][x] = cell
		self.full_data = data

	def print_stats(self):
		# Dictionary of cells and their amount of appearances in the table
		stats = {}

		for i, row in enumerate(self.full_data):
			for genotype in row:
				if genotype in stats:
					# The cell is already logged in the stats
					stats[genotype] += 1
				else:
					# The cell is not in the stats
					stats[genotype] = 1

		# Sort the stats by genotype
		stats = OrderedDict(sorted(stats.items()))
		total_items = sum(stats.values())
		for genotype, count in stats.items():
			prob = count / total_items * 100
			print(genotype + ": " + str(count) + " (" + str(prob) + "%)")
		return list(stats.keys())

