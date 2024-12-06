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

def get_unique_moves(input_file):
	directions = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1), }
	map_list = [list(row) for row in input_file]
	start_row, start_col, start_dir = get_initial_position(map_list, directions)
	visited = set()
	row, col, direction = start_row, start_col, start_dir
	visited.add((row, col))
	while 0 <= row < len(map_list) and 0 <= col < len(map_list[0]):
		dr, dc = directions[direction]
		next_row, next_col = row + dr, col + dc
		if 0 <= next_row < len(map_list) and 0 <= next_col < len(map_list[0]):
			if map_list[next_row][next_col] == '#':
				direction = change_direction(direction)
			else:
				row, col = next_row, next_col
				visited.add((row, col))
		else:
			break
	return len(visited)

def get_input(file_name):
	try:
		input_map = []
		with open(file_name, 'r') as file:
			for line in file:
				input_map.append(line.strip())		
		return input_map
	except FileNotFoundError:
		print("The file " + file_name + " does not exist.")
		exit()

if __name__ == "__main__":
	input_file = get_input("input.txt")
	unique_moves = get_unique_moves(input_file)
	print(f"guard visit before leaving the mapped area {unique_moves} distinct positions")