from itertools import combinations

def propagate_antinodes(start_point, diff, map_list, antinode):
				new_point = start_point
				while 0 <= new_point[0] < len(map_list[0]) and 0 <= new_point[1] < len(map_list):
					antinode.add(new_point)
					new_point = (new_point[0] + diff[0], new_point[1] + diff[1])

def get_antinode_number(map_list, antenna_coordinates):
	antinode = set()
	for antenna in antenna_coordinates:
		for antenna1, antenna2 in combinations(antenna_coordinates[antenna], 2):
			diff = (antenna2[0] - antenna1[0], antenna2[1] - antenna1[1])
			propagate_antinodes(antenna1, diff, map_list, antinode)
			propagate_antinodes(antenna1, (-diff[0], -diff[1]), map_list, antinode)
			propagate_antinodes(antenna2, diff, map_list, antinode)
			propagate_antinodes(antenna2, (-diff[0], -diff[1]), map_list, antinode)
	return len(antinode)

def get_antenna_coordinates(map_list):
	coordinates = {}
	for y, row in enumerate(map_list):
		for x, char in enumerate(row):
			if char != '.':
				if char not in coordinates:
					coordinates[char] = []
				coordinates[char].append((x, y))
	return coordinates

def get_input(file_name):
	try:
		input_map = []
		with open(file_name, 'r') as file:
			for line in file:
				input_map.append(line.strip())
		return [list(row) for row in input_map]    
	except FileNotFoundError:
		print("The file " + file_name + " does not exist.")
		exit()

if __name__ == "__main__":
	map_list = get_input("input.txt")
	antenna_coordinates = get_antenna_coordinates(map_list)
	antinode_number = get_antinode_number(map_list, antenna_coordinates)
	print(f"The number of antinodes is {antinode_number}")
