from heapq import heappop, heappush

def is_valid_move(maze, row, col):
	return 0 <= row < len(maze) and 0 <= col < len(maze[0]) and maze[row][col] != '#'

def solve_maze(maze, start, end):
	directions = [(-1, 0),(1, 0),(0, -1),(0, 1)]
	pq = []
	heappush(pq, (0, start, 3))
	visited = {}
	while pq:
		cost, current, direction = heappop(pq)
		if current == end:
			return cost
		if (current, direction) in visited and visited[(current, direction)] <= cost:
			continue
		visited[(current, direction)] = cost
		for i, (dy, dx) in enumerate(directions):
			new_row, new_col = current[0] + dy, current[1] + dx
			if is_valid_move(maze, new_row, new_col):
				rotation_cost = 1000 if i != direction else 0
				new_cost = cost + 1 + rotation_cost
				heappush(pq, (new_cost, (new_row, new_col), i))
	return -1

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
	minimum_score = solve_maze(maze, start, end)
	print(f"The lowest score possible is: {minimum_score}")