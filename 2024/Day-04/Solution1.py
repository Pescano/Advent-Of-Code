def search_from_position(x, y, word, rows, cols, grid):
	count = 0
	directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
	for dx, dy in directions:
		nx, ny = x, y
		for i in range(len(word)):
			if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == word[i]:
				nx += dx
				ny += dy
			else:
				break
		else:
			count += 1
	return count

def count_word_in_grid(grid, word):
	rows = len(grid)
	cols = len(grid[0]) if rows > 0 else 0
	total_count = 0
	for i in range(rows):
		for j in range(cols):
			total_count += search_from_position(i, j, word, rows, cols, grid)
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
	word_to_find = "XMAS"
	count = count_word_in_grid(input_file, word_to_find)
	print(f"The word '{word_to_find}' was found {count} times.")
