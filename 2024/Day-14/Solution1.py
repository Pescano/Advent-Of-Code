def get_quadrant_counts(future_positions, width, height):
	quadrant_counts = [0, 0, 0, 0]
	mid_x, mid_y = width // 2, height // 2
	for x, y in future_positions:
		if x == mid_x or y == mid_y:
			continue
		if x > mid_x and y > mid_y:
			quadrant_counts[0] += 1
		elif x < mid_x and y > mid_y:
			quadrant_counts[1] += 1
		elif x < mid_x and y < mid_y:
			quadrant_counts[2] += 1
		elif x > mid_x and y < mid_y:
			quadrant_counts[3] += 1
	return quadrant_counts

def get_future_positions(robots, time_steps, width, height):
	future_positions = []
	for (px, py), (vx, vy) in robots:
		nx = (px + vx * time_steps) % width
		ny = (py + vy * time_steps) % height
		future_positions.append((nx, ny))
	return future_positions

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
	time_steps = 100
	future_positions = get_future_positions(robots, time_steps, width, height)
	quadrant_counts = get_quadrant_counts(future_positions, width, height)
	print(f"The safety factor is {quadrant_counts[0] * quadrant_counts[1] * quadrant_counts[2] * quadrant_counts[3]}")
