def calculate_distances(list1, list2):
    sum_diff = 0
    for i in range(len(list1)):
        sum_diff += abs(list1[i] - list2[i])
    return sum_diff

def get_input(file_name):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            list1, list2 = [], []
            for line in lines:
                part1, part2 = line.split()
                list1.append(int(part1))
                list2.append(int(part2))
            return sorted(list1), sorted(list2)
    except FileNotFoundError:
        print("The file " + file_name + " does not exist.")
        exit()

if __name__ == "__main__":
    list1, list2 = get_input('input.txt')
    sum_diff = calculate_distances(list1, list2)
    print(sum_diff)
