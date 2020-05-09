from itertools import permutations
from punnettSquares import PunnettSquare

flowers = {
	'0': 'rryyww',
	'1': 'rryyWw',
	'3': 'rryyWW',
	'4': 'rrYyww',
	'5': 'rrYyWw',
	'7': 'rrYyWW',
	'0c': 'rrYYww',
	'0d': 'rrYYWw',
	'0f': 'rrYYWW',
	'10': 'Rryyww',
	'11': 'RryyWw',
	'13': 'RryyWW',
	'14': 'RrYyww',
	'15': 'RrYyWw',
	'17': 'RrYyWW',
	'1c': 'RrYYww',
	'1d': 'RrYYWw',
	'1f': 'RrYYWW',
	'30': 'RRyyww',
	'31': 'RRyyWw',
	'33': 'RRyyWW',
	'34': 'RRYyww',
	'35': 'RRYyWw',
	'37': 'RRYyWW',
	'3c': 'RRYYww',
	'3d': 'RRYYWw',
	'3f': 'RRYYWW'
}
tulips = {
	'0': 'White',
	'1': 'White (Seed)',
	'3': 'White',
	'4': 'Yellow',
	'5': 'Yellow',
	'7': 'White',
	'0c': 'Yellow (Seed)',
	'0d': 'Yellow',
	'0f': 'Yellow',
	'10': 'Red',
	'11': 'Pink',
	'13': 'White',
	'14': 'Orange',
	'15': 'Yellow',
	'17': 'Yellow',
	'1c': 'Orange',
	'1d': 'Yellow',
	'1f': 'Yellow',
	'30': 'Black',
	'31': 'Red (Seed)',
	'33': 'Red',
	'34': 'Black',
	'35': 'Red',
	'37': 'Red',
	'3c': 'Purple',
	'3d': 'Purple',
	'3f': 'Purple',
}
pansies = {
	'0': 'White',
	'1': 'White (Seed)',
	'3': 'Blue',
	'4': 'Yellow',
	'5': 'Yellow',
	'7': 'Blue',
	'0c': 'Yellow (Seed)',
	'0d': 'Yellow',
	'0f': 'Yellow',
	'10': 'Red',
	'11': 'Red',
	'13': 'Blue',
	'14': 'Orange',
	'15': 'Orange',
	'17': 'Orange',
	'1c': 'Yellow',
	'1d': 'Yellow',
	'1f': 'Yellow',
	'30': 'Red (Seed)',
	'31': 'Red',
	'33': 'Purple',
	'34': 'Red',
	'35': 'Red',
	'37': 'Purple',
	'3c': 'Orange',
	'3d': 'Orange',
	'3f': 'Purple'
}
cosmos = {
	'0': 'White',
	'1': 'White (Seed)',
	'3': 'White',
	'4': 'Yellow',
	'5': 'Yellow',
	'7': 'White',
	'0c': 'Yellow',
	'0d': 'Yellow (Seed)',
	'0f': 'Yellow',
	'10': 'Pink',
	'11': 'Pink',
	'13': 'Pink',
	'14': 'Orange',
	'15': 'Orange',
	'17': 'Pink',
	'1c': 'Orange',
	'1d': 'Orange',
	'1f': 'Orange',
	'30': 'Red (Seed)',
	'31': 'Red',
	'33': 'Red',
	'34': 'Orange',
	'35': 'Orange',
	'37': 'Red',
	'3c': 'Black',
	'3d': 'Black',
	'3f': 'Red'
}
lilies = {
	'0': 'White',
	'1': 'White',
	'3': 'White (Seed)',
	'4': 'Yellow',
	'5': 'White',
	'7': 'White',
	'0c': 'Yellow (Seed)',
	'0d': 'Yellow',
	'0f': 'White',
	'10': 'Red',
	'11': 'Pink',
	'13': 'White',
	'14': 'Orange',
	'15': 'Yellow',
	'17': 'Yellow',
	'1c': 'Orange',
	'1d': 'Yellow',
	'1f': 'Yellow',
	'30': 'Black',
	'31': 'Red (Seed)',
	'33': 'Pink',
	'34': 'Black',
	'35': 'Red',
	'37': 'Pink',
	'3c': 'Orange',
	'3d': 'Orange',
	'3f': 'White'
}
hyacinths = {
	'0': 'White',
	'1': 'White (Seed)',
	'3': 'Blue',
	'4': 'Yellow',
	'5': 'Yellow',
	'7': 'White',
	'0c': 'Yellow (Seed)',
	'0d': 'Yellow',
	'0f': 'Yellow',
	'10': 'Red',
	'11': 'Pink',
	'13': 'White',
	'14': 'Orange',
	'15': 'Yellow',
	'17': 'Yellow',
	'1c': 'Orange',
	'1d': 'Yellow',
	'1f': 'Yellow',
	'30': 'Red',
	'31': 'Red (Seed)',
	'33': 'Red',
	'34': 'Blue',
	'35': 'Blue',
	'37': 'Red',
	'3c': 'Purple',
	'3d': 'Purple',
	'3f': 'Purple'
}
windflowers = {
	'0': 'White',
	'1': 'White (Seed)',
	'3': 'Blue',
	'4': 'Orange',
	'5': 'Orange',
	'7': 'Blue',
	'0c': 'Orange (Seed)',
	'0d': 'Orange',
	'0f': 'Orange',
	'10': 'Red',
	'11': 'Red',
	'13': 'Blue',
	'14': 'Pink',
	'15': 'Pink',
	'17': 'Pink',
	'1c': 'Orange',
	'1d': 'Orange',
	'1f': 'Orange',
	'30': 'Red (Seed)',
	'31': 'Red',
	'33': 'Purple',
	'34': 'Red',
	'35': 'Red',
	'37': 'Purple',
	'3c': 'Pink',
	'3d': 'Pink',
	'3f': 'Purple'
}
mums = {
	'0': 'White',
	'1': 'White (Seed)',
	'3': 'Purple',
	'4': 'Yellow',
	'5': 'Yellow',
	'7': 'White',
	'0c': 'Yellow (Seed)',
	'0d': 'Yellow',
	'0f': 'Yellow',
	'10': 'Pink',
	'11': 'Pink',
	'13': 'Pink',
	'14': 'Yellow',
	'15': 'Red',
	'17': 'Pink',
	'1c': 'Purple',
	'1d': 'Purple',
	'1f': 'Purple',
	'30': 'Red (Seed)',
	'31': 'Red',
	'33': 'Red',
	'34': 'Purple',
	'35': 'Purple',
	'37': 'Red',
	'3c': 'Green',
	'3d': 'Green',
	'3f': 'Red'
}

print(len(flowers))


def pairings(parent_list):
	# Get all permutations of length 2
	hybridization_list = permutations(parent_list, 2)
	return hybridization_list


def find_children(parent_list):
	for i in list(parent_list):
		print(i)
		gen = PunnettSquare(i[0], i[1], flowers)
		gen.generateTable()
		print(gen.print_stats())


# Get all permutations of Level 0
perm = pairings(["1", "0c", "31"])

# Find lvl 1 children
find_children(perm)

# Print the obtained permutations


# Create Flower database
# List Flowers
# Determine lvl 0
# Log lvl 0 status
# Permutate lvl 0
# Determine lvl n
# Log lvl n valid parents
# Log lvl n status
# Permutate lvl n
# Determine lvl n+1 ...
# Return miniumum levels for all flowers


# Create Flower calculator
# Take input of desired flower color
# Determine flag(s) of desired color
# Get possible parents from database
# Iterate backwards until all parents are lvl 0
# Output full instructions with minimum steps.
