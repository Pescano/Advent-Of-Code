def causes_infinite_loop(map_list, directions):
	row, col, direction = get_initial_position(map_list, directions)
	visited = set()
	while 0 <= row < len(map_list) and 0 <= col < len(map_list[0]):
		if (row, col, direction) in visited:
			return True
		visited.add((row, col, direction))
		dr, dc = directions[direction]
		next_row, next_col = row + dr, col + dc
		if 0 <= next_row < len(map_list) and 0 <= next_col < len(map_list[0]):
			if map_list[next_row][next_col] == '#':
				direction = change_direction(direction)
			else:
				row, col = next_row, next_col
		else:
			break
	return False

def get_infinte_loop_points(map_list, directions, potencial_obstacules):
	infinite_loop_points = set()
	for point in potencial_obstacules:
		temp_map = [row[:] for row in map_list]
		temp_map[point[0]][point[1]] = '#'
		if causes_infinite_loop(temp_map, directions):
			infinite_loop_points.add(point)
	return len(infinite_loop_points)

def change_direction(current_direction):
	if current_direction == '^':
		return '>'
	elif current_direction == '>':
		return 'v'
	elif current_direction == 'v':
		return '<'
	elif current_direction == '<':
		return '^'

def get_initial_position(map_list, directions):
	for r in range(len(map_list)):
		for c in range(len(map_list[r])):
			if map_list[r][c] in directions:
				return r, c, map_list[r][c]

def get_potencial_obtacules(map_list, directions):
	potencial_obstacules = set()
	row, col, direction = get_initial_position(map_list, directions)
	while 0 <= row < len(map_list) and 0 <= col < len(map_list[0]):
		dr, dc = directions[direction]
		next_row, next_col = row + dr, col + dc
		if 0 <= next_row < len(map_list) and 0 <= next_col < len(map_list[0]):
			if map_list[next_row][next_col] == '#':
				direction = change_direction(direction)
			else:
				row, col = next_row, next_col
				for dr, dc in directions.values():
					if 0 <= next_row + dr < len(map_list) and 0 <= next_col + dc < len(map_list[0]) and map_list[next_row + dr][next_col + dc] == '.':
						potencial_obstacules.add((row + dr, col + dc))
		else:
			break
	return potencial_obstacules

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
	directions = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1), }
	potencial_obstacules = get_potencial_obtacules(map_list, directions)
	infinite_loop_points = get_infinte_loop_points(map_list, directions, potencial_obstacules)
	print(f"The number of infinite loop points is: {infinite_loop_points}")
