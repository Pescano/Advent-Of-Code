import re

def get_result(match_inputs):
	result = 0
	for match in match_inputs:
		numbers = match.split('(')[1].split(')')[0].split(',')
		result += int(numbers[0]) * int(numbers[1])
	return result

def get_input_match(input_file):
	pattern = re.compile("(mul\(\d{1,3}\,\d{1,3}\))")
	return pattern.findall(input_file)
def get_input(file_name):
	try:
		with open(file_name, 'r') as file:
			return file.read()
	except FileNotFoundError:
		print("The file " + file_name + " does not exist.")
		exit()

if __name__ == "__main__":
	input_file = get_input("input.txt")
	match_inputs = get_input_match(input_file)
	result = get_result(match_inputs)
	print(result)
