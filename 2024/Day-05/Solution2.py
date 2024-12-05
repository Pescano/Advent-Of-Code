def reordered_updates(rules, updates):
	reordered_updates = []
	for update in updates:
		new_update = update[:1]
		for i in range(1, len(update)):
			new_update.append(update[i])
			j = i
			while not is_valid_update(rules, new_update):
				new_update[j], new_update[j - 1] = new_update[j - 1], new_update[j]
				j -= 1
		reordered_updates.append(new_update[:])

	return reordered_updates

def get_middle_values_sum(updates):
	middle_values_sum = 0
	for update in updates:
		middle_values_sum += update[len(update) // 2]
	return middle_values_sum

def is_valid_update(rules, update):
	update_pos = {page: i for i, page in enumerate(update)}
	for x, y in rules:
		if x in update_pos and y in update_pos and update_pos[x] > update_pos[y]:
			return False
	return True

def get_invalid_updates(rules, updates):
	invalid_updates = []
	for update in updates:
		if not is_valid_update(rules, update):
			invalid_updates.append(update)
	return invalid_updates

def parsed_input(input_file):
	splitted = input_file.strip().split("\n\n")
	rules = [list(map(int, line.strip().split("|"))) for line in splitted[0].strip().split("\n")]
	updates = [list(map(int, line.strip().split(","))) for line in splitted[1].strip().split("\n")]
	return rules, updates

def get_input(file_name):
	try:
		with open(file_name, 'r') as file:
			return file.read()

	except FileNotFoundError:
		print("The file " + file_name + " does not exist.")
		exit()

if __name__ == "__main__":
	input_file = get_input("input.txt")
	rules, updates = parsed_input(input_file)
	invalid_updates = get_invalid_updates(rules, updates)
	reordered_updates = reordered_updates(rules, invalid_updates)
	middle_values_sum = get_middle_values_sum(reordered_updates)
	print(f"The sum of the middle values of the valid updates is {middle_values_sum}.")