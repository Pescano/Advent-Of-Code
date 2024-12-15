import numpy as np

def apply_expansion(warehouse_map):
	expanded_map = []
	tilemap = {'.': ['.', '.'], '@': ['@', '.'], 'O': ['[', ']'], '#': ['#', '#']}
	for row in warehouse_map:
		expanded_row = []
		for cell in row:
			expanded_row.extend(tilemap.get(cell, [cell, cell]))
		expanded_map.append(expanded_row)
	return expanded_map

def get_gps_sum(warehouse_map):
	gps_sum = 0
	for i in range(len(warehouse_map)):
		for j in range(len(warehouse_map[i])):
			if warehouse_map[i][j] == '[':
				gps_sum += 100 * i + j
	return gps_sum

def move_box_up_down(robot_pos, direction, warehouse_map):
	dir = direction
	if warehouse_map[robot_pos[0] + dir[0]][robot_pos[1] + dir[1]] == '.':
		warehouse_map[robot_pos[0] + dir[0]][robot_pos[1] + dir[1]] = '@'
		warehouse_map[robot_pos[0]][robot_pos[1]] = '.'
		robot_pos = (robot_pos[0] + dir[0], robot_pos[1] + dir[1])
	elif warehouse_map[robot_pos[0] + dir[0]][robot_pos[1] + dir[1]] in ['[', ']']:
		cand = [np.array([robot_pos[0] + dir[0], robot_pos[1] + dir[1]])]
		cluster = []
		while len(cand):
			check = cand.pop(0)
			if warehouse_map[check[0]][check[1]] == ']':
				cluster += [check, check + [0, -1]]
				cand += [check + [dir[0], 0], check + [dir[0], -1]]
			elif warehouse_map[check[0]][check[1]] == '[':
				cluster += [check, check + [0, 1]]
				cand += [check + [dir[0], 0], check + [dir[0], 1]]
		cluster = [np.array(item) for item in {tuple(arr) for arr in cluster}]
		blocked = False
		for element in cluster:
			if warehouse_map[element[0] + dir[0]][element[1] + dir[1]] == '#':
				blocked = True
				break
		if not blocked:
			for element in sorted(cluster, key=lambda x: x[0], reverse=dir[0] + 1):
				warehouse_map[element[0] + dir[0]][element[1] + dir[1]] = warehouse_map[element[0]][element[1]]
				warehouse_map[element[0]][element[1]] = '.'
			warehouse_map[robot_pos[0] + dir[0]][robot_pos[1] + dir[1]] = '@'
			warehouse_map[robot_pos[0]][robot_pos[1]] = '.'
			robot_pos = (robot_pos[0] + dir[0], robot_pos[1] + dir[1])
	return robot_pos, warehouse_map

def move_box_left_right(robot_pos, direction, warehouse_map):
	current_pos = robot_pos
	positions_to_update = []
	while True:
		next_pos = (current_pos[0] + direction[0], current_pos[1] + direction[1])
		if warehouse_map[next_pos[0]][next_pos[1]] == '#':
			break
		elif warehouse_map[next_pos[0]][next_pos[1]] == '.':
			positions_to_update.append(next_pos)
			break
		elif warehouse_map[next_pos[0]][next_pos[1]] == '[' or warehouse_map[next_pos[0]][next_pos[1]] == ']':
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
	directions = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}
	for command in commands:
		direction = directions[command]
		next_pos = (robot_pos[0] + direction[0], robot_pos[1] + direction[1])
		if warehouse_map[next_pos[0]][next_pos[1]] == '#':
			continue
		elif warehouse_map[next_pos[0]][next_pos[1]] == '.':
			warehouse_map[robot_pos[0]][robot_pos[1]] = '.'
			robot_pos = next_pos
			warehouse_map[robot_pos[0]][robot_pos[1]] = '@'
		elif warehouse_map[next_pos[0]][next_pos[1]] == '[' or warehouse_map[next_pos[0]][next_pos[1]] == ']':
			if command == '^' or command == 'v':
				robot_pos, warehouse_map = move_box_up_down(robot_pos, direction, warehouse_map)
			elif command == '<' or command == '>':
				robot_pos, warehouse_map = move_box_left_right(robot_pos, direction, warehouse_map)
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
	expanded_map = apply_expansion(warehouse_map)
	warehouse_map_future = calculate_future_position(expanded_map, commands)
	gps_sum = get_gps_sum(warehouse_map_future)
	print(f"The sum of all GPS coordinates is: {gps_sum}")