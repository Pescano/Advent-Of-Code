from heapq import heappop, heappush

def is_valid_move(maze, row, col):
	return 0 <= row < len(maze) and 0 <= col < len(maze[0]) and maze[row][col] != '#'

def dijkstra(maze, starts,directions):
	pq = []
	dist = {}
	for row, col, dir_idx in starts:
		dist[(row, col, dir_idx)] = 0
		heappush(pq, (0, row, col, dir_idx))
	while pq:
		cost, row, col, dir_idx = heappop(pq)
		if dist[(row, col, dir_idx)] < cost:
			continue
		for next_dir_idx, _ in enumerate(directions):
			if next_dir_idx != dir_idx:
				new_cost = cost + 1000
				state = (row, col, next_dir_idx)
				if state not in dist or dist[state] > new_cost:
					dist[state] = new_cost
					heappush(pq, (new_cost, row, col, next_dir_idx))
		new_row, new_col = row + directions[dir_idx][0], col + directions[dir_idx][1]
		if is_valid_move(maze, new_row, new_col):
			new_cost = cost + 1
			state = (new_row, new_col, dir_idx)
			if state not in dist or dist[state] > new_cost:
				dist[state] = new_cost
				heappush(pq, (new_cost, new_row, new_col, dir_idx))
	return dist

def solve_maze_bidirectional(maze, start, end):
	directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
	reverse_direction = {0: 1, 1: 0, 2: 3, 3: 2}
	from_start = dijkstra(maze, [(start[0], start[1], i) for i in range(4)], directions)
	from_end = dijkstra(maze, [(end[0], end[1], i) for i in range(4)], directions)
	optimal = min(from_start.get((end[0], end[1], i), float('inf')) for i in range(4))
	result = set()
	for row in range(len(maze)):
		for col in range(len(maze[0])):
			for dir_idx in range(4):
				forward_state = (row, col, dir_idx)
				backward_state = (row, col, reverse_direction[dir_idx])
				if (forward_state in from_start and backward_state in from_end and from_start[forward_state] + from_end[backward_state] == optimal):
					result.add((row, col))
	return len(result)

def get_input(file_name):
	try:
		with open(file_name, 'r') as f:
			maze = [line.strip() for line in f]
		start, end = None, None
		for r, row in enumerate(maze):
			for c, char in enumerate(row):
				if char == 'S':
					start = (r, c)
				elif char == 'E':
					end = (r, c)
		return maze, start, end
	except FileNotFoundError:
		print("The file " + file_name + " does not exist.")
		exit()

if __name__ == "__main__":
	maze, start, end = get_input("input.txt")
	result = solve_maze_bidirectional(maze, start, end)
	print(f"The number of optimal intersection points is: {result}")