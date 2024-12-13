from sympy import symbols, Eq, solve

def find_min_cost(ax, ay, bx, by, px, py):
	a, b = symbols('a b', integer=True)
	eq_x = Eq(ax * a + bx * b, px)
	eq_y = Eq(ay * a + by * b, py)
	solutions = solve((eq_x, eq_y), (a, b), dict=True)
	min_cost = float('inf')
	for sol in solutions:
		a_val = sol[a]
		b_val = sol[b]
		if a_val >= 0 and b_val >= 0 and a_val <= 100 and b_val <= 100:
			cost = 3 * a_val + b_val
			if cost < min_cost:
				min_cost = cost
	return min_cost if min_cost != float('inf') else None

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
				machines.append(((ax, ay), (bx, by), (px, py)))
		return machines
	except FileNotFoundError:
		print("The file " + file_name + " does not exist.")
		exit()

if __name__ == "__main__":
	machines = get_input("input.txt")
	total_cost = get_total_cost(machines)
	print(f"Total cost: {total_cost}")