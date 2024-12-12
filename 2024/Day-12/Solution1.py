def get_region(x, y, garden_type, visited, map, moves, col, row):
	stack = [(x, y)]
	area = 0
	fences = 0
	while stack:
		cx, cy = stack.pop()
		if visited[cx][cy]:
			continue
		visited[cx][cy] = True
		area += 1
		for dx, dy in moves:
			nx, ny = cx + dx, cy + dy			
			if not is_inside(nx, ny, row,col) or map[nx][ny] != garden_type:
				fences += 1
			elif not visited[nx][ny]:
				stack.append((nx, ny))
	return area, fences

def is_inside(x, y, col, row):
	return 0 <= x < row and 0 <= y < col

def get_total_price(map):
	row = len(map)
	col = len(map[0])
	moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
	visited = [[False] * col for _ in range(row)]
	total_price = 0
	for i in range(row):
		for j in range(col):
			if not visited[i][j]:
				garden_type = map[i][j]
				area, fences = get_region(i, j, garden_type, visited, map, moves, col, row)
				total_price += area * fences
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