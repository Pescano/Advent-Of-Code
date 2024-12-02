def is_in_valid_range(report, report_type):
	for i in range(1, len(report)):
		diff = report[i] - report[i-1]
		if report_type == "increasing" and not (1 <= diff <= 3):
			return False
		elif report_type == "decreasing" and not (1 <= -diff <= 3):
			return False
	return True

def is_monotonic(list_numbers):
	increasing = decreasing = True
	for i in range(1, len(list_numbers)):
		if list_numbers[i] < list_numbers[i-1]:
			increasing = False
		if list_numbers[i] > list_numbers[i-1]:
			decreasing = False
	return "increasing" if increasing else "decreasing" if decreasing else "neither"

def get_reports_safe(list_reports):
	total_reports = 0
	for report in list_reports:
		report_type = is_monotonic(report)
		if (report_type) != "neither":
			if is_in_valid_range(report, report_type):
				total_reports += 1 
			else:
				for i in range(0, len(report)):
					report_copy = report.copy()
					report_copy.pop(i)
					if is_in_valid_range(report_copy, report_type):
						total_reports += 1
	return total_reports

def get_input(file_name):
	try:
		with open(file_name, 'r') as file:
			lines = file.readlines()
			list_reports = []
			for line in lines:
				line_list = list(map(int, line.split()))
				list_reports.append(line_list)
			return list_reports
	except FileNotFoundError:
		print("The file " + file_name + " does not exist.")
		exit()

if __name__ == "__main__":
	list_reports = get_input("input.txt")
	reports_safe = get_reports_safe(list_reports)
	print("The number of reports that are safe is: " + str(reports_safe))