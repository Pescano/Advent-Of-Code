def blink(stones_dict):
	new_stones_dict = {}
	for stone, count in stones_dict.items():
		if stone == 0:
			if 1 not in new_stones_dict:
				new_stones_dict[1] = 0
			new_stones_dict[1] += count
		elif len(str(stone)) % 2 == 0:
			half_len = len(str(stone)) // 2
			left_half = int(str(stone)[:half_len])
			right_half = int(str(stone)[half_len:])
			if left_half not in new_stones_dict:
				new_stones_dict[left_half] = 0
			if right_half not in new_stones_dict:
				new_stones_dict[right_half] = 0
			new_stones_dict[left_half] += count
			new_stones_dict[right_half] += count
		else:
			new_value = stone * 2024
			if new_value not in new_stones_dict:
				new_stones_dict[new_value] = 0
			new_stones_dict[new_value] += count
	return new_stones_dict

def get_total_stones(input_stones, blinks):
	stones_dict = {}
	for stone in input_stones:
		if stone not in stones_dict:
			stones_dict[stone] = 0
		stones_dict[stone] += 1
	for i in range(blinks):
		stones_dict = blink(stones_dict)
	return sum(stones_dict.values())

def get_input(file_name):
	try:
		with open(file_name, 'r') as file:
			return [int(x) for x in file.read().strip().split()]
	except FileNotFoundError:
		print(f"The file {file_name} does not exist.")
		exit()

if __name__ == "__main__":
	input_stones = get_input("input.txt")
	blinks = 75
	total_stones = get_total_stones(input_stones, blinks)
	print(f"Total stones after {blinks} blinks: {total_stones}")
