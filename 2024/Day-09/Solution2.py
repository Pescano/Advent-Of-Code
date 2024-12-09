def get_checksum(disk_defragmented):
	checksum = 0
	for i in range(len(disk_defragmented)):
		if disk_defragmented[i] != '.':
			checksum += disk_defragmented[i] * i
	return checksum

def get_disk_defragmented(disk_fragmented):
	disk_defragmented = disk_fragmented.copy()
	i = len(disk_defragmented) - 1
	while i >= 0:
		if disk_defragmented[i] != '.':
			value = disk_defragmented[i]
			j = i
			while j >= 0 and disk_defragmented[j] == value:
				j -= 1
			j += 1
			space_needed = i - j + 1
			current_space_index = 0
			move = False
			while current_space_index < j:
				while current_space_index < j and disk_defragmented[current_space_index] != '.':
					current_space_index += 1
				final_space_index = current_space_index
				while final_space_index < j and disk_defragmented[final_space_index] == '.':
					final_space_index += 1
				total_space = final_space_index - current_space_index
				if total_space >= space_needed:
					move = True
					break
				else:
					current_space_index = final_space_index
			if move:
				for k in range(i, j - 1, -1):
					disk_defragmented[current_space_index] = disk_defragmented[k]
					disk_defragmented[k] = '.'
					current_space_index += 1
			i = j
		i -= 1
	return disk_defragmented

def get_disk_fragmented(disk_map):
	disk_fragmented = []
	is_file = True
	for i in range(len(disk_map)):
		if is_file:
			for j in range(disk_map[i]):
				disk_fragmented.append(i//2)
		else:
			for j in range(disk_map[i]):
				disk_fragmented.append(".")
		is_file = not is_file
	return disk_fragmented

def get_input(file_name):
	try:
		with open(file_name, 'r') as file:
			return [int(char) for char in file.read().strip()]
	except FileNotFoundError:
		print("The file " + file_name + " does not exist.")
		exit()

if __name__ == "__main__":
	disk_map = get_input("input.txt")
	disk_fragmented = get_disk_fragmented(disk_map)
	disk_defragmented = get_disk_defragmented(disk_fragmented)
	checksum = get_checksum(disk_defragmented)
	print(f"The checksum is: {checksum}")