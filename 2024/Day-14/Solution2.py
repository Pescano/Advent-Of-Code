def print_map(positions, width, height):
	grid = [["." for _ in range(width)] for _ in range(height)]
	for pos in positions:
		x, y = pos
		grid[y][x] = "#"
	for row in grid:
		print("".join(row))

def get_future_positions(robots, time_steps, width, height):
	future_positions = []
	for (px, py), (vx, vy) in robots:
		nx = (px + vx * time_steps) % width
		ny = (py + vy * time_steps) % height
		future_positions.append((nx, ny))
	return future_positions

def get_easter_egg_time(robots, width, height):
	easter_egg_time = 0
	while True:
		future_positions = get_future_positions(robots, easter_egg_time, width, height)
		distinct_positions = set(future_positions)
		if len(distinct_positions) == len(future_positions):
			break
		easter_egg_time += 1
	return easter_egg_time, future_positions

def get_input(file_name):
	try:
		robots = []
		with open(file_name, 'r') as file:
			for line in file:
				pos, vel = line.strip().split(" v=")
				px, py = map(int, pos[2:].split(","))
				vx, vy = map(int, vel.split(","))
				robots.append(((px, py), (vx, vy)))
		return robots
	except FileNotFoundError:
		print("The file " + file_name + " does not exist.")
		exit()

if __name__ == "__main__":
	robots = get_input("input.txt")
	width, height = 101, 103
	easter_egg_time, easter_egg_map = get_easter_egg_time(robots, width, height)
	print(f"The easter egg will appear at time {easter_egg_time}")
	print_map(easter_egg_map, width, height)
