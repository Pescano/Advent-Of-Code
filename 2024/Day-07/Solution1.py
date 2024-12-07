import itertools

def validated_operation(key, values, operations):
    result = int(values[0])
    for i in range(len(operations)):
        if operations[i] == '+':
            result += int(values[i + 1])
        elif operations[i] == '*':
            result *= int(values[i + 1])
    return result == int(key)

def get_valid_operations_result(input_file):
	valid_operations_sum = 0
	for key in input_file:
		operations = itertools.product(['+', '*'], repeat=len(input_file[key]) - 1)
		for operation in operations:
			if validated_operation(key, input_file[key], operation):
				valid_operations_sum += int(key)
				break
	return valid_operations_sum

def get_input(file_name):
	try:
		input_map = {}
		with open(file_name, 'r') as file:
			for line in file:
				line_splited = line.strip().split(":")
				input_map[line_splited[0]] = line_splited[1].strip().split(" ")
		return input_map
	except FileNotFoundError:
		print("The file " + file_name + " does not exist.")
		exit()

if __name__ == "__main__":
	input_file = get_input("input.txt")
	result = get_valid_operations_result(input_file)
	print(f"The sum of the results of the valid operations is: {result}")