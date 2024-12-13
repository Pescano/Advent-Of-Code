def find_min_cost(ax, ay, bx, by, px, py):
	b = (px*ay-py*ax)//(ay*bx-by*ax)
	a = (px*by-py*bx)//(by*ax-bx*ay)
	cost = None
	if ax * a + bx * b == px and ay * a + by * b == py:
		cost = 3 * a + b
	return cost

def get_total_cost(machines):
	total_cost = 0
	for machine in machines:
		(ax, ay), (bx, by), (px, py) = machine
		cost = find_min_cost(ax, ay, bx, by, px, py)
		if cost is not None:
			total_cost += cost
	return total_cost

def get_input(file_name):
	try:
		machines = []
		with open(file_name, 'r') as f:
			lines = f.readlines()
			for i in range(0, len(lines), 4):
				ax, ay = map(int, lines[i].strip().split('X+')[1].split(', Y+'))
				bx, by = map(int, lines[i+1].strip().split('X+')[1].split(', Y+'))
				px, py = map(int, lines[i+2].strip().split('X=')[1].split(', Y='))
				px += 10000000000000
				py += 10000000000000
				machines.append(((ax, ay), (bx, by), (px, py)))
		return machines
	except FileNotFoundError:
		print("The file " + file_name + " does not exist.")
		exit()

if __name__ == "__main__":
	machines = get_input("input.txt")
	total_cost = get_total_cost(machines)
	print(f"Total cost: {total_cost}")