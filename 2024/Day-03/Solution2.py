import re

def get_mul(match):
	numbers = match.split('(')[1].split(')')[0].split(',')
	return int(numbers[0]) * int(numbers[1])

def get_result(match_inputs):
	result = 0
	enables = True
	for match in match_inputs:
		if "mul" in match.group() and enables:
			result += get_mul(match.group())
		elif "do()" in match.group():
			enables = True
		elif "don't()" in match.group():
			enables = False		
	return result

def get_input_match(input_file):	
	patterns = [re.compile(r"mul\(\d{1,3},\d{1,3}\)"), re.compile(r"\bdo\(\)"), re.compile(r"\bdon't\(\)")]
	matchs = re.finditer(f"({'|'.join([pattern.pattern for pattern in patterns])})", input_file)
	return matchs

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
