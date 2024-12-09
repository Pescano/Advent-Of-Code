def get_checksum(disk_defragmented):
	checksum = 0
	for i in range(len(disk_defragmented)):
		if disk_defragmented[i] != '.':
			checksum += disk_defragmented[i] * i
	return checksum

def get_disk_defragmented(disk_fragmented):
	disk_defragmented = disk_fragmented.copy()
	for i in range(len(disk_defragmented) - 1, -1, -1):
		if disk_defragmented[i] != '.':
			for j in range(i):
				if disk_defragmented[j] == '.':
					disk_defragmented[j] = disk_defragmented[i]
					disk_defragmented[i] = '.'
					break
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
