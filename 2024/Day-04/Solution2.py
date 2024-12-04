def count_word_in_grid(grid):
	rows = len(grid) -1
	cols = len(grid[0]) - 1 if rows > 0 else 0
	total_count = 0
	for i in range(1, rows):
		for j in range(1, cols):
			if grid[i][j] == 'A' and {grid[i - 1][j - 1], grid[i + 1][j + 1]} == {'M', 'S'} and {grid[i + 1][j - 1], grid[i - 1][j + 1]} == {'M', 'S'}:
				total_count += 1
	return total_count

def get_input(file_name):
	try:
		with open(file_name, 'r') as file:
			data = []
			for line in file:
				data.append(line.strip())
			return data

	except FileNotFoundError:
		print("The file " + file_name + " does not exist.")
		exit()

if __name__ == "__main__":
	input_file = get_input("input.txt")
	count = count_word_in_grid(input_file)
	print(f"The word 'X-MAX' was found {count} times.")