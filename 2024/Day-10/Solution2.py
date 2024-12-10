from collections import deque

def get_trail_score(map_list, start_position):
	rows, cols = len(map_list), len(map_list[0])
	directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
	queue = deque([(start_position[0], start_position[1])])
	reachable_trailhead = 0	
	while queue:
		x, y = queue.popleft()
		if int(map_list[x][y]) == 9:
			reachable_trailhead += 1
		for dx, dy in directions:
			nx, ny = x + dx, y + dy
			if 0 <= nx < rows and 0 <= ny < cols and (nx, ny):
				if int(map_list[nx][ny]) == int(map_list[x][y]) + 1:
					queue.append((nx, ny))
	return reachable_trailhead

def get_trailhead_score(map_list, start_positions):
	trailhead_score = 0
	for start_position in start_positions:
		trailhead_score += get_trail_score(map_list, start_position)
	return trailhead_score

def get_start_positions(map_list):
	start_positions = []
	for i in range(len(map_list)):
		for j in range(len(map_list[i])):
			if map_list[i][j] == "0":
				start_positions.append((i, j))
	return start_positions

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
	start_position_list = get_start_positions(map_list)
	trailhead_score = get_trailhead_score(map_list, start_position_list)
	print(f"The trailhead score is: {trailhead_score}")