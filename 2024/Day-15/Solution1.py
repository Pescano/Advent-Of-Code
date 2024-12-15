def get_gps_sum(warehouse_map):
	gps_sum = 0
	for i in range(len(warehouse_map)):
		for j in range(len(warehouse_map[i])):
			if warehouse_map[i][j] == 'O':
				gps_sum += 100 * i + j
	return gps_sum

def move_box(robot_pos, direction, warehouse_map):
	current_pos = robot_pos
	positions_to_update = []
	while True:
		next_pos = (current_pos[0] + direction[0], current_pos[1] + direction[1])
		if warehouse_map[next_pos[0]][next_pos[1]] == '#':
			break
		elif warehouse_map[next_pos[0]][next_pos[1]] == '.':
			positions_to_update.append(next_pos)
			break
		elif warehouse_map[next_pos[0]][next_pos[1]] == 'O':
			positions_to_update.append(next_pos)
			current_pos = next_pos
		else:
			break
	if len(positions_to_update) > 0 and warehouse_map[positions_to_update[-1][0]][positions_to_update[-1][1]] == '.':
		for i in range(len(positions_to_update) - 1, -1, -1):
			prev = robot_pos if i == 0 else positions_to_update[i - 1]
			warehouse_map[positions_to_update[i][0]][positions_to_update[i][1]] = warehouse_map[prev[0]][prev[1]]
		warehouse_map[robot_pos[0]][robot_pos[1]] = '.'
		robot_pos = (robot_pos[0] + direction[0], robot_pos[1] + direction[1])
		warehouse_map[robot_pos[0]][robot_pos[1]] = '@'
	return robot_pos, warehouse_map

def get_starting_position(warehouse_map):
	for i in range(len(warehouse_map)):
		for j in range(len(warehouse_map[i])):
			if warehouse_map[i][j] == '@':
				return (i, j)

def calculate_future_position(warehouse_map, commands):
	robot_pos = get_starting_position(warehouse_map)
	directions = {'^': (-1, 0),'v': (1, 0),'<': (0, -1),'>': (0, 1)}
	for command in commands:
		direction = directions[command]
		next_pos = (robot_pos[0] + direction[0], robot_pos[1] + direction[1])
		if warehouse_map[next_pos[0]][next_pos[1]] == '#':
			continue
		elif warehouse_map[next_pos[0]][next_pos[1]] == '.':
			warehouse_map[robot_pos[0]][robot_pos[1]] = '.'
			robot_pos = next_pos
			warehouse_map[robot_pos[0]][robot_pos[1]] = '@'
		elif warehouse_map[next_pos[0]][next_pos[1]] == 'O':
			robot_pos, warehouse_map = move_box(robot_pos, direction, warehouse_map)
	return warehouse_map

def get_parse_input(file_name):
	try:
		map_lines = []
		commands = []
		with open(file_name, 'r') as file:
			lines = file.readlines()
			for line in lines:
				line = line.strip()
				if line.startswith('#'):
					map_lines.append(list(line))
				else:
					commands.append(line)
			commands = ''.join(commands)
		return map_lines, commands
	except FileNotFoundError:
		print("The file " + file_name + " does not exist.")
		exit()

if __name__ == "__main__":
	warehouse_map, commands = get_parse_input("input.txt")
	warehouse_map_future = calculate_future_position(warehouse_map, commands)
	gps_sum = get_gps_sum(warehouse_map_future)
	print(f"The sum of all GPS coordinates is: {gps_sum}")
