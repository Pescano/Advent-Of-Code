def blink(stones):
	new_stones = []
	for stone in stones:
		if stone == 0:
			new_stones.append(1)
		elif len(str(stone)) % 2 == 0:
			half_len = len(str(stone)) // 2
			left_half = int(str(stone)[:half_len])
			right_half = int(str(stone)[half_len:])
			new_stones.append(left_half)
			new_stones.append(right_half)
		else:
			new_stones.append(stone * 2024)
	return new_stones

def get_total_stones(input_stones, blinks):
	stones = input_stones
	for _ in range(blinks):
		stones = blink(stones)
	return len(stones)

def get_input(file_name):
	try:
		with open(file_name, 'r') as file:
			return [int(x) for x in file.read().strip().split()]
	except FileNotFoundError:
		print("The file " + file_name + " does not exist.")
		exit()

if __name__ == "__main__":
	input_stones = get_input("input.txt")
	blinks = 25
	total_stones = get_total_stones(input_stones, blinks)
	print(f"Total stones after {blinks} blinks: {total_stones}")
