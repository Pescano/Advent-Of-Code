from collections import deque

def build_zone(start, map):
	row, col = len(map), len(map[0])
	queue = deque([start])
	start_point = map[start[1]][start[0]]
	zone = set([start])
	directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
	while queue:
		x, y = queue.popleft()
		for dx, dy in directions:
			nx, ny = x + dx, y + dy
			if 0 <= nx < col and 0 <= ny < row and (nx, ny) not in zone:
				if map[ny][nx] == start_point:
					zone.add((nx, ny))
					queue.append((nx, ny))
	return zone

def calculate_zone_corners(zone, map):
	corners = 0
	for x, y in zone:
		N = (x, y-1) in zone
		E = (x+1, y) in zone
		S = (x, y+1) in zone
		W = (x-1, y) in zone
		NE = (x+1, y-1) in zone
		SE = (x+1, y+1) in zone
		NW = (x-1, y-1) in zone
		SW = (x-1, y+1) in zone
		if not N and not E and not S and not W:
			corners += 4
		if N and not E and not S and not W:
			corners += 2
		if E and not S and not W and not N:
			corners += 2
		if S and not W and not N and not E:
			corners += 2
		if W and not N and not E and not S:
			corners += 2
		if S and E and not N and not W:
			corners += 1
		if S and W and not N and not E:
			corners += 1
		if N and E and not S and not W:
			corners += 1
		if N and W and not S and not E:
			corners += 1
		if E and N and not NE:
			corners += 1
		if E and S and not SE:
			corners += 1
		if W and N and not NW:
			corners += 1
		if W and S and not SW:
			corners += 1
	return corners

def get_total_price(map):
	checked = set()
	total_price = 0
	for y in range(len(map)):
		for x in range(len(map[0])):
			if (x, y) not in checked:
				zone = build_zone((x, y), map)
				area = len(zone)
				corners = calculate_zone_corners(zone, map)
				total_price += area * corners
				checked.update(zone)
	return total_price

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
	total_price = get_total_price(map_list)
	print(f"The total price is: {total_price}")